# Generated by Django 5.0.6 on 2024-07-15 20:25

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Authorisation', '0001_initial'),
        ('Inventory', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=128)),
                ('quantity', models.PositiveIntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('UOM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uoms', to='Inventory.unitofmeasurecategory')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_companies', to='Authorisation.company')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.product')),
                ('purchase_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='Inventory.purchaseorder')),
            ],
        ),
        migrations.CreateModel(
            name='RequestForQuotation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('vendor_reference', models.CharField(max_length=255)),
                ('currency', models.CharField(max_length=10)),
                ('order_deadline', models.DateField()),
                ('expected_arrival', models.DateField()),
                ('deliver_to', models.CharField(max_length=255)),
                ('taxes', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('tax_excluded', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=10)),
                ('reference', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_rfqs', to=settings.AUTH_USER_MODEL)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authorisation.company')),
            ],
        ),
        migrations.CreateModel(
            name='RFQProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authorisation.company')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.product')),
                ('rfq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='purchase.requestforquotation')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('individual', 'Individual'), ('company', 'Company')], max_length=10)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('company_name', models.CharField(max_length=255)),
                ('contact_street1', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_street2', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_city', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_state', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_zip', models.CharField(blank=True, max_length=10, null=True)),
                ('contact_country', models.CharField(blank=True, max_length=255, null=True)),
                ('tax_id', models.CharField(blank=True, max_length=255, null=True)),
                ('job_position', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('tags', models.CharField(blank=True, max_length=255, null=True)),
                ('vendor_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authorisation.company')),
            ],
        ),
        migrations.AddField(
            model_name='requestforquotation',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase.vendor'),
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('orderDate', models.DateField()),
                ('orderDeadline', models.DateField()),
                ('ExpectedArrival', models.DateField()),
                ('Currency', models.CharField(max_length=120)),
                ('PurchaseOrderNo', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=128)),
                ('Discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('SubtotallessDiscount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('TaxRate', models.CharField(max_length=5)),
                ('TotalTax', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Shipping', models.DecimalField(decimal_places=2, max_digits=10)),
                ('OtherCosts', models.DecimalField(decimal_places=2, max_digits=10)),
                ('GrandTotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('CompanyAddress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='po_addresses', to='Authorisation.company')),
                ('CompanyEmail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_emails', to='Authorisation.company')),
                ('CompanyName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_names', to='Authorisation.company')),
                ('CompanyPhone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_phones', to='Authorisation.company')),
                ('CompanyWebsite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_websites', to='Authorisation.company')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_order_products', to='purchase.purchaseorderproduct')),
                ('VendorAddress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_addresses', to='purchase.vendor')),
                ('VendorCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_companies', to='purchase.vendor')),
                ('VendorEmail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_emails', to='purchase.vendor')),
                ('VendorName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_names', to='purchase.vendor')),
                ('VendorNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_numbers', to='purchase.vendor')),
                ('VendorPhone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_phones', to='purchase.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='VendorPriceList',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('vendor', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(max_length=10)),
                ('valid_from', models.DateField()),
                ('valid_to', models.DateField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authorisation.company')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_price_lists', to='Inventory.product')),
            ],
        ),
    ]
