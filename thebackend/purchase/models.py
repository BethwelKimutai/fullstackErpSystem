from django.db import models
from django.contrib.auth.models import User
from accounts.models import Company
from inventory.models import Product  # Assuming the Product model is in the inventory app

class Vendor(models.Model):
    VENDOR_TYPE_CHOICES = [
        ('individual', 'Individual'),
        ('company', 'Company')
    ]

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

class RequestForQuotation(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    vendor_reference = models.CharField(max_length=255)
    currency = models.CharField(max_length=10)
    order_deadline = models.DateField()
    expected_arrival = models.DateField()
    deliver_to = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    taxes = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tax_excluded = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    reference = models.CharField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        self.total = self.tax_excluded + self.taxes
        super().save(*args, **kwargs)

class PurchaseOrder(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    vendor_reference = models.CharField(max_length=255)
    currency = models.CharField(max_length=10)
    order_deadline = models.DateField()
    expected_arrival = models.DateField()
    deliver_to = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    taxes = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tax_excluded = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    reference = models.CharField(max_length=255, unique=True)
    confirmation_date = models.DateField(auto_now_add=True)
    source_document = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        self.total = self.tax_excluded + self.taxes
        super().save(*args, **kwargs)

