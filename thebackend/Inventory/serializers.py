from rest_framework import serializers
from .models import Product, ProductCategory, ProductTemplate, ReplenishOrder, PurchaseOrder, Inventory, Receipt, \
    Delivery, InternalTransfer, PhysicalInventory, Scrap, LandedCost


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTemplate
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ReplenishOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplenishOrder
        fields = '__all__'


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'


class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = '__all__'


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'


class InternalTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternalTransfer
        fields = '__all__'


class PhysicalInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalInventory
        fields = '__all__'


class ScrapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scrap
        fields = '__all__'


class LandedCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandedCost
        fields = '__all__'
