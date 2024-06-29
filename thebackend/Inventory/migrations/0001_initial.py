# Generated by Django 5.0.6 on 2024-06-28 16:45

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Authorisation', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductTemplate',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BarcodeNomenclature',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('pattern', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authorisation.company')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('product_type', models.CharField(max_length=255)),
                ('invoice_policy', models.CharField(max_length=255)),
                ('unit_of_measure', models.CharField(max_length=50)),
                ('purchase_uom', models.CharField(max_length=50)),
                ('sales_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customer_taxes', models.CharField(max_length=255)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('internal_reference', models.CharField(max_length=255)),
                ('barcode', models.CharField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authorisation.company')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.productcategory')),
                ('product_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.producttemplate')),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalInventory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=255)),
                ('on_hand_quantity', models.PositiveIntegerField()),
                ('counted_quantity', models.PositiveIntegerField()),
                ('difference', models.IntegerField()),
                ('scheduled_date', models.DateField()),
                ('unit', models.CharField(max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authorisation.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.product')),
            ],
        ),
        migrations.CreateModel(
            name='LandedCost',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('transfers', models.CharField(max_length=255)),
                ('journal', models.CharField(max_length=255)),
                ('vendor_bill', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('account', models.CharField(max_length=255)),
                ('split_method', models.CharField(max_length=255)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('name', models.CharField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authorisation.company')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.product')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('responsible', models.CharField(max_length=255)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('volume', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customer_lead_time', models.PositiveIntegerField()),
                ('hs_code', models.CharField(max_length=50)),
                ('origin_of_goods', models.CharField(max_length=255)),
                ('packaging', models.CharField(max_length=255)),
                ('container', models.CharField(max_length=255)),
                ('unit_of_measure', models.CharField(max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authorisation.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.product')),
            ],
        ),
        migrations.CreateModel(
            name='InternalTransfer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('document_number', models.CharField(max_length=255, unique=True)),
                ('source_location', models.CharField(max_length=255)),
                ('destination_location', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('scheduled_date', models.DateField()),
                ('source_document', models.CharField(max_length=255)),
                ('packaging', models.CharField(max_length=255)),
                ('demand', models.PositiveIntegerField()),
                ('unit', models.CharField(max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authorisation.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.product')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('document_number', models.CharField(max_length=255, unique=True)),
                ('source_location', models.CharField(max_length=255)),
                ('destination_location', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('scheduled_date', models.DateField()),
                ('source_document', models.CharField(max_length=255)),
                ('packaging', models.CharField(max_length=255)),
                ('demand', models.PositiveIntegerField()),
                ('unit', models.CharField(max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authorisation.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authorisation.company')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_attributes', to='Inventory.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPackaging',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('packaging_type', models.CharField(max_length=255)),
                ('dimensions', models.CharField(max_length=255)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('volume', models.DecimalField(decimal_places=2, max_digits=10)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authorisation.company')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_packagings', to='Inventory.product')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('vendor', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(max_length=10)),
                ('delivery_delay', models.PositiveIntegerField()),
                ('order_date', models.DateField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authorisation.company')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('contact', models.CharField(max_length=255)),
                ('operation_type', models.CharField(choices=[('IN', 'Incoming'), ('OUT', 'Outgoing'), ('TRANSFER', 'Internal Transfer')], max_length=10)),
                ('source_location', models.CharField(max_length=255)),
                ('destination_location', models.CharField(max_length=255)),
                ('scheduled_date', models.DateField()),
                ('source_document', models.CharField(max_length=255)),
                ('packaging', models.CharField(max_length=255)),
                ('demand', models.PositiveIntegerField()),
                ('unit', models.CharField(max_length=50)),
                ('document_number', models.CharField(max_length=255, unique=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authorisation.company')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReorderingRule',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('min_quantity', models.PositiveIntegerField()),
                ('max_quantity', models.PositiveIntegerField()),
                ('reorder_quantity', models.PositiveIntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authorisation.company')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reoredering_rules', to='Inventory.product')),
            ],
        ),
        migrations.CreateModel(
            name='ReplenishOrder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('order_quantity', models.PositiveIntegerField()),
                ('order_date', models.DateField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authorisation.company')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Scrap',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField()),
                ('source_location', models.CharField(max_length=255)),
                ('scrap_location', models.CharField(max_length=255)),
                ('source_document', models.CharField(max_length=255)),
                ('replenish_quantities', models.BooleanField()),
                ('document_number', models.CharField(max_length=255, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('unit', models.CharField(max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authorisation.company')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.product')),
            ],
        ),
        migrations.CreateModel(
            name='UnitOfMeasureCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authorisation.company')),
            ],
        ),
    ]
