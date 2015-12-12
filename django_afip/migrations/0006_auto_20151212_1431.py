# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-12 14:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_afip.models


class Migration(migrations.Migration):

    dependencies = [
        ('afip', '0005_auto_20150918_0115'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceiptEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=128, verbose_name='description')),
                ('amount', models.PositiveSmallIntegerField(verbose_name='amount')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='unit price')),
            ],
            options={
                'verbose_name': 'receipt entry',
                'verbose_name_plural': 'receipt entries',
            },
        ),
        migrations.CreateModel(
            name='ReceiptPDF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_file', models.FileField(null=True, upload_to='', verbose_name='pdf file')),
                ('issuing_name', models.TextField(verbose_name='issuing name')),
                ('issuing_address', models.TextField(verbose_name='issuing address')),
                ('issuing_email', models.TextField(null=True, verbose_name='issuing address')),
                ('vat_condition', models.CharField(max_length=48, verbose_name='vat condition')),
                ('gross_income_condition', models.CharField(max_length=48, verbose_name='gross income condition')),
                ('client_name', models.TextField(verbose_name='client name')),
                ('client_address', models.TextField(verbose_name='client address')),
                ('sales_terms', models.CharField(max_length=48, verbose_name='sales terms')),
            ],
            options={
                'verbose_name': 'receipt pdf',
                'verbose_name_plural': 'receipt pdfs',
            },
        ),
        migrations.CreateModel(
            name='TaxPayerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issuing_name', models.TextField(verbose_name='issuing name')),
                ('issuing_address', models.TextField(verbose_name='issuing address')),
                ('vat_condition', models.CharField(max_length=48, verbose_name='vat condition')),
                ('gross_income_condition', models.CharField(max_length=48, verbose_name='gross income condition')),
            ],
        ),
        migrations.AlterModelOptions(
            name='authticket',
            options={'verbose_name': 'authorization ticket', 'verbose_name_plural': 'authorization tickets'},
        ),
        migrations.AlterModelOptions(
            name='concepttype',
            options={'verbose_name': 'concept type', 'verbose_name_plural': 'concept types'},
        ),
        migrations.AlterModelOptions(
            name='currencytype',
            options={'verbose_name': 'currency type', 'verbose_name_plural': 'currency types'},
        ),
        migrations.AlterModelOptions(
            name='documenttype',
            options={'verbose_name': 'document type', 'verbose_name_plural': 'document types'},
        ),
        migrations.AlterModelOptions(
            name='observation',
            options={'verbose_name': 'observation', 'verbose_name_plural': 'observations'},
        ),
        migrations.AlterModelOptions(
            name='pointofsales',
            options={'verbose_name': 'point of sales', 'verbose_name_plural': 'points of sales'},
        ),
        migrations.AlterModelOptions(
            name='receipt',
            options={'verbose_name': 'receipt', 'verbose_name_plural': 'receipts'},
        ),
        migrations.AlterModelOptions(
            name='receiptbatch',
            options={'verbose_name': 'receipt batch', 'verbose_name_plural': 'receipt batches'},
        ),
        migrations.AlterModelOptions(
            name='receipttype',
            options={'verbose_name': 'receipt type', 'verbose_name_plural': 'receipt types'},
        ),
        migrations.AlterModelOptions(
            name='receiptvalidation',
            options={'verbose_name': 'receipt validation', 'verbose_name_plural': 'receipt validations'},
        ),
        migrations.AlterModelOptions(
            name='tax',
            options={'verbose_name': 'tax', 'verbose_name_plural': 'taxes'},
        ),
        migrations.AlterModelOptions(
            name='taxpayer',
            options={'verbose_name': 'taxpayer', 'verbose_name_plural': 'taxpayers'},
        ),
        migrations.AlterModelOptions(
            name='taxtype',
            options={'verbose_name': 'tax type', 'verbose_name_plural': 'tax types'},
        ),
        migrations.AlterModelOptions(
            name='validation',
            options={'verbose_name': 'validation', 'verbose_name_plural': 'validations'},
        ),
        migrations.AlterModelOptions(
            name='vat',
            options={'verbose_name': 'vat', 'verbose_name_plural': 'vat'},
        ),
        migrations.AlterModelOptions(
            name='vattype',
            options={'verbose_name': 'vat type', 'verbose_name_plural': 'vat types'},
        ),
        migrations.AddField(
            model_name='taxpayer',
            name='active_since',
            field=models.DateField(help_text='Date since which this taxpayer has been legally active. This field is only required to generate receipt PDFs', null=True, verbose_name='active since'),
        ),
        migrations.AlterField(
            model_name='authticket',
            name='expires',
            field=models.DateTimeField(default=django_afip.models.AuthTicket.default_expires, verbose_name='expires'),
        ),
        migrations.AlterField(
            model_name='authticket',
            name='generated',
            field=models.DateTimeField(default=django_afip.models.AuthTicket.default_generated, verbose_name='generated'),
        ),
        migrations.AlterField(
            model_name='authticket',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auth_tickets', to='afip.TaxPayer', verbose_name='owner'),
        ),
        migrations.AlterField(
            model_name='authticket',
            name='service',
            field=models.CharField(help_text='Service for which this ticket has been authorized', max_length=6, verbose_name='service'),
        ),
        migrations.AlterField(
            model_name='authticket',
            name='signature',
            field=models.TextField(verbose_name='signature'),
        ),
        migrations.AlterField(
            model_name='authticket',
            name='unique_id',
            field=models.IntegerField(default=django_afip.models.AuthTicket.default_unique_id, verbose_name='unique id'),
        ),
        migrations.AlterField(
            model_name='concepttype',
            name='code',
            field=models.CharField(max_length=3, verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='concepttype',
            name='description',
            field=models.CharField(max_length=250, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='concepttype',
            name='valid_from',
            field=models.DateField(blank=True, null=True, verbose_name='valid from'),
        ),
        migrations.AlterField(
            model_name='concepttype',
            name='valid_to',
            field=models.DateField(blank=True, null=True, verbose_name='valid until'),
        ),
        migrations.AlterField(
            model_name='currencytype',
            name='code',
            field=models.CharField(max_length=3, verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='currencytype',
            name='description',
            field=models.CharField(max_length=250, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='currencytype',
            name='valid_from',
            field=models.DateField(blank=True, null=True, verbose_name='valid from'),
        ),
        migrations.AlterField(
            model_name='currencytype',
            name='valid_to',
            field=models.DateField(blank=True, null=True, verbose_name='valid until'),
        ),
        migrations.AlterField(
            model_name='documenttype',
            name='code',
            field=models.CharField(max_length=3, verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='documenttype',
            name='description',
            field=models.CharField(max_length=250, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='documenttype',
            name='valid_from',
            field=models.DateField(blank=True, null=True, verbose_name='valid from'),
        ),
        migrations.AlterField(
            model_name='documenttype',
            name='valid_to',
            field=models.DateField(blank=True, null=True, verbose_name='valid until'),
        ),
        migrations.AlterField(
            model_name='observation',
            name='code',
            field=models.PositiveSmallIntegerField(verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='observation',
            name='message',
            field=models.CharField(max_length=255, verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='pointofsales',
            name='blocked',
            field=models.BooleanField(verbose_name='blocked'),
        ),
        migrations.AlterField(
            model_name='pointofsales',
            name='drop_date',
            field=models.DateField(blank=True, null=True, verbose_name='drop date'),
        ),
        migrations.AlterField(
            model_name='pointofsales',
            name='issuance_type',
            field=models.CharField(help_text='Indicates if thie POS emits using CAE and CAEA.', max_length=8, verbose_name='issuance type'),
        ),
        migrations.AlterField(
            model_name='pointofsales',
            name='number',
            field=models.PositiveSmallIntegerField(verbose_name='number'),
        ),
        migrations.AlterField(
            model_name='pointofsales',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afip.TaxPayer', verbose_name='owner'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='batch',
            field=models.ForeignKey(blank=True, help_text='Receipts are validated in batches, so it must be assigned one before validation is possible.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='receipts', to='afip.ReceiptBatch', verbose_name='receipt batch'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='concept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receipts', to='afip.ConceptType', verbose_name='concept'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='currency',
            field=models.ForeignKey(help_text='Currency in which this receipt is issued.', on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='afip.CurrencyType', verbose_name='currency'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='currency_quote',
            field=models.DecimalField(decimal_places=6, help_text='Quote of the day for the currency used in the receipt', max_digits=10, verbose_name='currency quote'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='document_number',
            field=models.BigIntegerField(help_text='The document number of the customer to whom this receipt is addressed', verbose_name='document number'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='document_type',
            field=models.ForeignKey(help_text='The document type of the customer to whom this receipt is addressed', on_delete=django.db.models.deletion.CASCADE, related_name='receipts', to='afip.DocumentType', verbose_name='document type'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='exempt_amount',
            field=models.DecimalField(decimal_places=2, help_text='Only for categories which are tax-exempt. For C-type receipts, this must be zero.', max_digits=15, verbose_name='exempt amount'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='expiration_date',
            field=models.DateField(blank=True, help_text='Date on which this receipt expires. No applicable for goods.', null=True, verbose_name='receipt expiration date'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='issued_date',
            field=models.DateField(help_text='Can diverge up to 5 days for good, or 10 days otherwise', verbose_name='issued date'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='net_taxed',
            field=models.DecimalField(decimal_places=2, help_text='The total amount to which taxes apply. For C-type receipts, this is equal to the subtotal.', max_digits=15, verbose_name='total taxable amount'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='net_untaxed',
            field=models.DecimalField(decimal_places=2, help_text='The total amount to which taxes do not apply. For C-type receipts, this must be zero.', max_digits=15, verbose_name='total untaxable amount'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='point_of_sales',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receipts', to='afip.PointOfSales', verbose_name='point of sales'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='receipt_number',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='receipt number'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='receipt_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receipts', to='afip.ReceiptType', verbose_name='receipt type'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='related_receipts',
            field=models.ManyToManyField(blank=True, to='afip.Receipt', verbose_name='related receipts'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='service_end',
            field=models.DateField(blank=True, help_text='Date on which a service ended. No applicable for goods.', null=True, verbose_name='service end date'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='service_start',
            field=models.DateField(blank=True, help_text='Date on which a service started. No applicable for goods.', null=True, verbose_name='service start date'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, help_text='Must be equal to untaxed amount + exempt amount + taxes + vat.', max_digits=15, verbose_name='total amount'),
        ),
        migrations.AlterField(
            model_name='receiptbatch',
            name='point_of_sales',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afip.PointOfSales', verbose_name='point of sales'),
        ),
        migrations.AlterField(
            model_name='receiptbatch',
            name='receipt_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afip.ReceiptType', verbose_name='receipt type'),
        ),
        migrations.AlterField(
            model_name='receipttype',
            name='code',
            field=models.CharField(max_length=3, verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='receipttype',
            name='description',
            field=models.CharField(max_length=250, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='receipttype',
            name='valid_from',
            field=models.DateField(blank=True, null=True, verbose_name='valid from'),
        ),
        migrations.AlterField(
            model_name='receipttype',
            name='valid_to',
            field=models.DateField(blank=True, null=True, verbose_name='valid until'),
        ),
        migrations.AlterField(
            model_name='receiptvalidation',
            name='cae_expiration',
            field=models.DateField(verbose_name='cae expiration'),
        ),
        migrations.AlterField(
            model_name='receiptvalidation',
            name='observations',
            field=models.ManyToManyField(related_name='valiations', to='afip.Observation', verbose_name='observations'),
        ),
        migrations.AlterField(
            model_name='receiptvalidation',
            name='receipt',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='validation', to='afip.Receipt', verbose_name='receipt'),
        ),
        migrations.AlterField(
            model_name='receiptvalidation',
            name='result',
            field=models.CharField(choices=[('A', 'approved'), ('R', 'rejected'), ('P', 'partial')], max_length=1, verbose_name='result'),
        ),
        migrations.AlterField(
            model_name='receiptvalidation',
            name='validation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receipts', to='afip.Validation', verbose_name='validation'),
        ),
        migrations.AlterField(
            model_name='tax',
            name='aliquot',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='aliquot'),
        ),
        migrations.AlterField(
            model_name='tax',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='amount'),
        ),
        migrations.AlterField(
            model_name='tax',
            name='base_amount',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='base amount'),
        ),
        migrations.AlterField(
            model_name='tax',
            name='description',
            field=models.CharField(max_length=80, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='tax',
            name='tax_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afip.TaxType', verbose_name='tax type'),
        ),
        migrations.AlterField(
            model_name='taxpayer',
            name='certificate',
            field=models.FileField(null=True, upload_to='', verbose_name='certificate'),
        ),
        migrations.AlterField(
            model_name='taxpayer',
            name='key',
            field=models.FileField(null=True, upload_to='', verbose_name='key'),
        ),
        migrations.AlterField(
            model_name='taxpayer',
            name='name',
            field=models.CharField(help_text='A friendly name to recognize this taxpayer.', max_length=32, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='taxtype',
            name='code',
            field=models.CharField(max_length=3, verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='taxtype',
            name='description',
            field=models.CharField(max_length=250, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='taxtype',
            name='valid_from',
            field=models.DateField(blank=True, null=True, verbose_name='valid from'),
        ),
        migrations.AlterField(
            model_name='taxtype',
            name='valid_to',
            field=models.DateField(blank=True, null=True, verbose_name='valid until'),
        ),
        migrations.AlterField(
            model_name='validation',
            name='batch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='validation', to='afip.ReceiptBatch', verbose_name='receipt batch'),
        ),
        migrations.AlterField(
            model_name='validation',
            name='processed_date',
            field=models.DateTimeField(verbose_name='processed date'),
        ),
        migrations.AlterField(
            model_name='validation',
            name='result',
            field=models.CharField(choices=[('A', 'approved'), ('R', 'rejected'), ('P', 'partial')], max_length=1, verbose_name='result'),
        ),
        migrations.AlterField(
            model_name='vat',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='amount'),
        ),
        migrations.AlterField(
            model_name='vat',
            name='base_amount',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='base amount'),
        ),
        migrations.AlterField(
            model_name='vat',
            name='vat_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afip.VatType', verbose_name='vat type'),
        ),
        migrations.AlterField(
            model_name='vattype',
            name='code',
            field=models.CharField(max_length=3, verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='vattype',
            name='description',
            field=models.CharField(max_length=250, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='vattype',
            name='valid_from',
            field=models.DateField(blank=True, null=True, verbose_name='valid from'),
        ),
        migrations.AlterField(
            model_name='vattype',
            name='valid_to',
            field=models.DateField(blank=True, null=True, verbose_name='valid until'),
        ),
        migrations.AddField(
            model_name='taxpayerprofile',
            name='taxpayer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='afip.TaxPayer', verbose_name='taxpayer'),
        ),
        migrations.AddField(
            model_name='receiptpdf',
            name='receipt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afip.Receipt', verbose_name='receipt'),
        ),
        migrations.AddField(
            model_name='receiptentry',
            name='receipt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='afip.Receipt', verbose_name='receipt'),
        ),
    ]
