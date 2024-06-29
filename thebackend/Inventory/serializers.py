from rest_framework import serializers
from .models import (Product, ProductCategory, ProductTemplate, ReplenishOrder, PurchaseOrder, Inventory, Receipt,
                     Delivery, InternalTransfer, PhysicalInventory, Scrap, LandedCost, ProductAttribute,
                     UnitOfMeasureCategory
, ProductPackaging, ReorderingRule, BarcodeNomenclature)


class ProductCategorySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex')
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = ProductCategory
        fields = ['id','name', 'description', 'company', 'company_name']


class ProductTemplateSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex')
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = ProductTemplate
        fields = ['name', 'description']


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex')
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'product_type', 'invoice_policy', 'unit_of_measure', 'purchase_uom', 'sales_price',
                  'customer_taxes', 'cost', 'product_category', 'internal_reference', 'barcode', 'product_template',
                  'company']


class ReplenishOrderSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex')

    class Meta:
        model = ReplenishOrder
        fields = ['id', 'product', 'order_quantity', 'order_date', 'company', 'user']


class PurchaseOrderSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex')

    class Meta:
        model = PurchaseOrder
        fields = ['id', 'product', 'vendor', 'price', 'currency', 'delivery_delay', 'order_date', 'company', 'user']


class InventorySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex')

    class Meta:
        model = Inventory
        fields = ['id', 'product', 'responsible', 'weight', 'volume', 'customer_lead_time', 'hs_code',
                  'origin_of_goods', 'packaging', 'container', 'unit_of_measure', 'company', 'user']


class ReceiptSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex')

    class Meta:
        model = Receipt
        fields = ['id', 'contact', 'operation_type', 'source_location', 'destination_location', 'scheduled_date',
                  'source_document', 'product', 'packaging', 'demand', 'unit', 'company', 'document_number', 'user']


class DeliverySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex')

    class Meta:
        model = Delivery
        fields = ['id', 'document_number', 'source_location', 'destination_location', 'contact', 'scheduled_date',
                  'source_document', 'company', 'product', 'packaging', 'demand', 'unit', 'user']


class InternalTransferSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex')

    class Meta:
        model = InternalTransfer
        fields = ['id', 'document_number', 'source_location', 'destination_location', 'contact', 'scheduled_date',
                  'source_document', 'company', 'product', 'packaging', 'demand', 'unit', 'user']


class PhysicalInventorySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex')

    class Meta:
        model = PhysicalInventory
        fields = ['id', 'location', 'product', 'on_hand_quantity', 'counted_quantity', 'difference', 'scheduled_date',
                  'unit', 'user', 'company']


class ScrapSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex')

    class Meta:
        model = Scrap
        fields = ['id', 'product', 'quantity', 'source_location', 'scrap_location', 'source_document', 'company',
                  'replenish_quantities', 'document_number', 'date', 'unit']


class LandedCostSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex')

    class Meta:
        model = LandedCost
        fields = ['id', 'date', 'transfers', 'journal', 'company', 'vendor_bill', 'product', 'description', 'account',
                  'split_method', 'cost', 'name']


class ProductAttributeSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex')
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = ProductAttribute
        fields = ['id', 'name', 'value', 'product','company', 'company_name']


class UnitOfMeasureCategorySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex')
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = UnitOfMeasureCategory
        fields = ['id', 'name', 'description', 'company', 'company_name']


class ProductPackagingSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex')
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = ProductPackaging
        fields = ['id', 'product', 'packaging_type', 'dimensions', 'weight', 'volume']


class ReorderingRuleSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex')
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = ReorderingRule
        fields = ['id', 'product', 'min_quantity', 'max_quantity', 'reorder_quantity','company', 'company_name']


class BarcodeNomenclatureSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex')
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = BarcodeNomenclature
        fields = ['id', 'name', 'description', 'pattern','company', 'company_name']
