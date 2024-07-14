from django.contrib import admin
from .models import Vendor, RequestForQuotation, PurchaseOrderProduct, PurchaseOrder, RFQProduct, VendorPriceList

# Register your models here.

admin.site.register(Vendor)
admin.site.register(RequestForQuotation)
admin.site.register(PurchaseOrderProduct)
admin.site.register(PurchaseOrder)
admin.site.register(RFQProduct)
admin.site.register(VendorPriceList)
