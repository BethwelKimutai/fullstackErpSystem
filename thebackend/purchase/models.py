import uuid

from django.db import models
from django.contrib.auth.models import User

import settings
from Authorisation.models import Company
from Inventory.models import Product  # Assuming the Product model is in the inventory app


class Vendor(models.Model):
    VENDOR_TYPE_CHOICES = [
        ('individual', 'Individual'),
        ('company', 'Company')
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=10, choices=VENDOR_TYPE_CHOICES)
    name = models.CharField(max_length=255, null=True, blank=True)
    company_name = models.CharField(max_length=255)
    contact_street1 = models.CharField(max_length=255, null=True, blank=True)
    contact_street2 = models.CharField(max_length=255, null=True, blank=True)
    contact_city = models.CharField(max_length=255, null=True, blank=True)
    contact_state = models.CharField(max_length=255, null=True, blank=True)
    contact_zip = models.CharField(max_length=10, null=True, blank=True)
    contact_country = models.CharField(max_length=255, null=True, blank=True)
    tax_id = models.CharField(max_length=255, null=True, blank=True)
    job_position = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    tags = models.CharField(max_length=255, null=True, blank=True)
    vendor_company = models.ForeignKey(Company, on_delete=models.CASCADE)


class RequestForQuotation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    vendor_reference = models.CharField(max_length=255)
    currency = models.CharField(max_length=10)
    order_deadline = models.DateField()
    expected_arrival = models.DateField()
    deliver_to = models.CharField(max_length=255)
    taxes = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tax_excluded = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='purchase_rfqs')
    reference = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total = self.tax_excluded + self.taxes
        super().save(*args, **kwargs)


class PurchaseOrder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    vendor_reference = models.CharField(max_length=255)
    currency = models.CharField(max_length=10)
    order_deadline = models.DateField()
    expected_arrival = models.DateField()
    deliver_to = models.CharField(max_length=255)
    taxes = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tax_excluded = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='purchase_purchase_orders')
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                              related_name='purchase_purchase_orders')
    reference = models.CharField(max_length=255, unique=True)
    confirmation_date = models.DateField(auto_now_add=True)
    source_document = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total = self.tax_excluded + self.taxes
        super().save(*args, **kwargs)


class PurchaseOrderProduct(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class RFQProduct(models.Model):
    rfq = models.ForeignKey(RequestForQuotation, on_delete=models.CASCADE, related_name='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class VendorPriceList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vendor = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='vendor_price_lists')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    valid_from = models.DateField()
    valid_to = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
