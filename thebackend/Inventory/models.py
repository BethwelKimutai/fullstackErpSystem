from django.db import models
from django.contrib.auth.models import User
from Authorisation.models import Company


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

class ProductTemplate(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    invoice_policy = models.CharField(max_length=255)
    unit_of_measure = models.CharField(max_length=50)
    purchase_uom = models.CharField(max_length=50)
    sales_price = models.DecimalField(max_digits=10, decimal_places=2)
    customer_taxes = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    internal_reference = models.CharField(max_length=255)
    barcode = models.CharField(max_length=255)
    product_template = models.ForeignKey(ProductTemplate, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class ReplenishOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_quantity = models.PositiveIntegerField()
    order_date = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class PurchaseOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    vendor = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    delivery_delay = models.PositiveIntegerField()
    order_date = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    responsible = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.DecimalField(max_digits=10, decimal_places=2)
    customer_lead_time = models.PositiveIntegerField()
    hs_code = models.CharField(max_length=50)
    origin_of_goods = models.CharField(max_length=255)
    packaging = models.CharField(max_length=255)
    container = models.CharField(max_length=255)
    unit_of_measure = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Receipt(models.Model):
    OPERATION_TYPES = [
        ('IN', 'Incoming'),
        ('OUT', 'Outgoing'),
        ('TRANSFER', 'Internal Transfer')
    ]

    contact = models.CharField(max_length=255)
    operation_type = models.CharField(choices=OPERATION_TYPES, max_length=10)
    source_location = models.CharField(max_length=255)
    destination_location = models.CharField(max_length=255)
    scheduled_date = models.DateField()
    source_document = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    packaging = models.CharField(max_length=255)
    demand = models.PositiveIntegerField()
    unit = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    document_number = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Delivery(models.Model):
    document_number = models.CharField(max_length=255, unique=True)
    source_location = models.CharField(max_length=255)
    destination_location = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    scheduled_date = models.DateField()
    source_document = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    packaging = models.CharField(max_length=255)
    demand = models.PositiveIntegerField()
    unit = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class InternalTransfer(models.Model):
    document_number = models.CharField(max_length=255, unique=True)
    source_location = models.CharField(max_length=255)
    destination_location = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    scheduled_date = models.DateField()
    source_document = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    packaging = models.CharField(max_length=255)
    demand = models.PositiveIntegerField()
    unit = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class PhysicalInventory(models.Model):
    location = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    on_hand_quantity = models.PositiveIntegerField()
    counted_quantity = models.PositiveIntegerField()
    difference = models.IntegerField()
    scheduled_date = models.DateField()
    unit = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Scrap(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    source_location = models.CharField(max_length=255)
    scrap_location = models.CharField(max_length=255)
    source_document = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    replenish_quantities = models.BooleanField()
    document_number = models.CharField(max_length=255, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    unit = models.CharField(max_length=50)


class LandedCost(models.Model):
    date = models.DateField()
    transfers = models.CharField(max_length=255)
    journal = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    vendor_bill = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.TextField()
    account = models.CharField(max_length=255)
    split_method = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=255)

