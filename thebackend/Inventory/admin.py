from django.contrib import admin
from .models import (
    ProductCategory, ProductTemplate, Product, ReplenishOrder, PurchaseOrder,
    Inventory, Receipt, Delivery, InternalTransfer, PhysicalInventory, Scrap,
    LandedCost, ProductAttribute, UnitOfMeasureCategory, ProductPackaging,
    ReorderingRule, BarcodeNomenclature
)

# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(ProductTemplate)
admin.site.register(Product)
admin.site.register(ReplenishOrder)
admin.site.register(PurchaseOrder)
admin.site.register(Inventory)
admin.site.register(Receipt)
admin.site.register(Delivery)
admin.site.register(InternalTransfer)
admin.site.register(PhysicalInventory)
admin.site.register(Scrap)
admin.site.register(LandedCost)
admin.site.register(ProductAttribute)
admin.site.register(UnitOfMeasureCategory)
admin.site.register(ProductPackaging)
admin.site.register(ReorderingRule)
admin.site.register(BarcodeNomenclature)
