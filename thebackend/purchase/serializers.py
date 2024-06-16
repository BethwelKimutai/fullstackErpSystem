from rest_framework import serializers
from .models import Vendor, RequestForQuotation, PurchaseOrder

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class RequestForQuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestForQuotation
        fields = '__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
