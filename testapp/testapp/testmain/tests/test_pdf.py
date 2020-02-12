import os
import re
from io import BytesIO

from barcode.writer import SVGWriter
from django.test import TestCase
from lxml import etree

from django_afip import factories, models
from django_afip.pdf import ReceiptBarcodeGenerator


class ReceiptPDFGenerationTestCase(TestCase):
    def test_pdf_generation(self):
        """
        Test PDF file generation.

        For the moment, this test case mostly verifies that pdf generation
        *works*, but does not actually validate the pdf file itself.

        Running this locally *will* yield the file itself, which is useful for
        manual inspection.
        """
        pdf = factories.ReceiptPDFFactory(receipt__receipt_number=3)
        factories.ReceiptValidationFactory(receipt=pdf.receipt)
        pdf.save_pdf()
        regex = r'afip/receipts/[a-f0-9]{2}/[a-f0-9]{2}/[a-f0-9]{32}.pdf'
        self.assertTrue(re.match(regex, pdf.pdf_file.name))
        self.assertTrue(pdf.pdf_file.name.endswith('.pdf'))

    def test_unauthorized_receipt_generation(self):
        """
        Test PDF file generation for unauthorized receipts.

        Confirm that attempting to generate a PDF for an unauthorized receipt
        raises.
        """
        taxpayer = factories.TaxPayerFactory()
        factories.TaxPayerProfileFactory(taxpayer=taxpayer)
        receipt = factories.ReceiptFactory(
            receipt_number=None,
            point_of_sales__owner=taxpayer,
        )
        pdf = models.ReceiptPDF.objects.create_for_receipt(
            receipt=receipt,
            client_name='John Doe',
            client_address='12 Green Road\nGreenville\nUK',
        )
        with self.assertRaisesMessage(
            Exception,
            'Cannot generate pdf for non-authorized receipt'
        ):
            pdf.save_pdf()


class BarcodeGeneratorVerificationDigitTestCase(TestCase):
    def assert_verification_digit(self, number, digit):
        number = [int(n) for n in number]
        self.assertEqual(
            ReceiptBarcodeGenerator.verification_digit(number),
            digit,
        )

    def test_verfification_digit(self):
        self.assert_verification_digit('01234567890', 5)
        self.assert_verification_digit(
            '123456789012345678901234567890123456789',
            0,
        )
        self.assert_verification_digit(
            '111111111112233334444444444444455555555',
            3,
        )
        self.assert_verification_digit(
            '202468793631100026719363618010820170512',
            9
        )


def make_xml_canonical(xml_lines):
    """Returns an XML with attributes in cannonical order."""
    parser = etree.XMLParser(remove_blank_text=True)

    xml = etree.fromstring(b''.join(xml_lines), parser)

    xml_bytes = BytesIO()
    xml.getroottree().write_c14n(xml_bytes)
    return xml_bytes.getvalue()


class BarcodeGeneratorTestCase(TestCase):
    def test_generate_barcode(self):
        """
        Test that barcode generation matches that from a pre-generated example.
        """
        receipt = factories.ReceiptFactory(
            point_of_sales__number=1,
            receipt_type__code=11,
        )
        factories.ReceiptValidationFactory(receipt=receipt,)

        generator = ReceiptBarcodeGenerator(receipt)
        barcode = generator.generate_barcode(SVGWriter)

        # Remove the line that stamps the pyBarcode version
        # Otherwise this test will break as soon as a new release comes out.
        lines = [
            line for line in barcode.splitlines()
            if b'Autogenerated with python-barcode' not in line
        ]

        directory = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(directory, 'barcode.svg')

        with open(path, 'rb') as f:
            self.assertEqual(
                make_xml_canonical(lines),
                make_xml_canonical(f.read().splitlines()),
            )


class GenerateReceiptPDFSignalTestCase(TestCase):
    def test_not_validated_receipt(self):
        printable = factories.ReceiptPDFFactory()

        self.assertFalse(printable.pdf_file)

    def test_validated_receipt(self):
        validation = factories.ReceiptValidationFactory()
        printable = factories.ReceiptPDFFactory(receipt=validation.receipt)

        self.assertTrue(printable.pdf_file)
        self.assertTrue(printable.pdf_file.name.endswith('.pdf'))
