import uuid

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import AccessToken

from Authorisation.models import Company
from purchase.models import VendorPriceList
from purchase.serializers import VendorPriceListSerializer
from .models import Product, Receipt, Delivery, InternalTransfer, PhysicalInventory, Scrap, LandedCost, \
    UnitOfMeasureCategory, ProductPackaging, ReorderingRule, BarcodeNomenclature, ProductAttribute
from .serializers import (ProductSerializer, ReceiptSerializer, DeliverySerializer,
                          InternalTransferSerializer, PhysicalInventorySerializer,
                          ScrapSerializer, LandedCostSerializer, ProductAttributeSerializer,
                          UnitOfMeasureCategorySerializer, ProductPackagingSerializer, ReorderingRuleSerializer,
                          BarcodeNomenclatureSerializer)

from .models import Product, ProductCategory, ProductTemplate, ReplenishOrder, PurchaseOrder, Inventory
from .serializers import (ProductSerializer, ProductCategorySerializer, ProductTemplateSerializer,
                          ReplenishOrderSerializer, PurchaseOrderSerializer, InventorySerializer)


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(company=user.company)

    @action(detail=False, methods=['post'])
    def create_product(self, request):
        try:
            data = request.data
            serializer = ProductSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f"Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'])
    def get_products(self, request):
        products = self.get_queryset()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def update_product(self, request, pk=None):
        try:
            product = self.get_object()
            data = request.data.copy()
            serializer = ProductSerializer(product, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f"Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['delete'])
    def delete_product(self, request, pk=None):
        try:
            product = self.get_object()
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"message": f"Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['post'])
    def replenish(self, request):
        data = request.data
        company_id = request.COOKIES.get('company_id')
        user_id = request.COOKIES.get('id')
        data['company'] = company_id
        data['user'] = user_id
        serializer = ReplenishOrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def purchase(self, request):
        data = request.data
        company_id = request.COOKIES.get('company_id')
        user_id = request.COOKIES.get('id')
        data['company'] = company_id
        data['user'] = user_id
        serializer = PurchaseOrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get', 'post'])
    def inventory(self, request):
        if request.method == 'POST':
            data = request.data
            company_id = request.COOKIES.get('company_id')
            user_id = request.COOKIES.get('id')
            data['company'] = company_id
            data['user'] = user_id
            serializer = InventorySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            inventories = Inventory.objects.filter(company=request.user.company)
            serializer = InventorySerializer(inventories, many=True)
            return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def get_product_categories(self, request):
        categories = self.get_queryset()
        serializer = ProductCategorySerializer(categories, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def create_product_category(self, request):
        token = request.COOKIE.get('jwt')

        data = request.data
        print(data)
        serializer = ProductCategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'])
    def update_product_category(self, request, pk=None):
        try:
            product_category = self.get_object()
            data = request.data.copy()
            serializer = ProductCategorySerializer(product_category, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['delete'])
    def delete_product_category(self, request, pk=None):
        try:
            product_category = self.get_object()
            product_category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"message": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['post'])
    def create_product_template(self, request):
        data = request.data
        serializer = ProductTemplateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def get_product_templates(self, request):
        templates = self.get_queryset()
        serializer = ProductTemplateSerializer(templates, many=True)
        return Response(serializer.data)


class ReceiptViewSet(viewsets.ModelViewSet):
    serializer_class = ReceiptSerializer

    def get_queryset(self):
        user = self.request.user
        return Receipt.objects.filter(company=user.company)

    @action(detail=False, methods=['post'])
    def create_receipt(self, request):
        data = request.data.copy()
        data['company'] = request.user.company_id
        data['user'] = request.user.id
        serializer = ReceiptSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def get_receipts(self, request):
        receipts = self.get_queryset()
        serializer = ReceiptSerializer(receipts, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def update_receipt(self, request, pk=None):
        try:
            receipt = self.get_object()
            data = request.data.copy()
            serializer = ReceiptSerializer(receipt, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f"Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['delete'])
    def delete_receipt(self, request, pk=None):
        try:
            receipt = self.get_object()
            receipt.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"message": f"Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeliveryViewSet(viewsets.ModelViewSet):
    serializer_class = DeliverySerializer

    def get_queryset(self):
        user = self.request.user
        return Delivery.objects.filter(company=user.company)

    @action(detail=False, methods=['post'])
    def create_delivery(self, request):
        data = request.data.copy()
        data['company'] = request.user.company_id
        data['user'] = request.user.id
        serializer = DeliverySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def get_deliveries(self, request):
        deliveries = self.get_queryset()
        serializer = DeliverySerializer(deliveries, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def update_delivery(self, request, pk=None):
        try:
            delivery = self.get_object()
            data = request.data.copy()
            serializer = DeliverySerializer(delivery, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f"Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['delete'])
    def delete_delivery(self, request, pk=None):
        try:
            delivery = self.get_object()
            delivery.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"message": f"Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class InternalTransferViewSet(viewsets.ModelViewSet):
    serializer_class = InternalTransferSerializer

    def get_queryset(self):
        user = self.request.user
        return InternalTransfer.objects.filter(company=user.company)

    @action(detail=False, methods=['post'])
    def create_internal_transfer(self, request):
        data = request.data.copy()
        data['company'] = request.user.company_id
        data['user'] = request.user.id
        serializer = InternalTransferSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def get_internal_transfers(self, request):
        internal_transfers = self.get_queryset()
        serializer = InternalTransferSerializer(internal_transfers, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def update_internal_transfer(self, request, pk=None):
        try:
            internal_transfer = self.get_object()
            data = request.data.copy()
            serializer = InternalTransferSerializer(internal_transfer, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f"Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['delete'])
    def delete_internal_transfer(self, request, pk=None):
        try:
            internal_transfer = self.get_object()
            internal_transfer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"message": f"Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PhysicalInventoryViewSet(viewsets.ModelViewSet):
    serializer_class = PhysicalInventorySerializer

    def get_queryset(self):
        user = self.request.user
        return PhysicalInventory.objects.filter(company=user.company)

    @action(detail=False, methods=['post'])
    def create_physical_inventory(self, request):
        data = request.data.copy()
        data['company'] = request.user.company_id
        data['user'] = request.user.id
        data['difference'] = data.get('counted_quantity', 0) - data.get('on_hand_quantity', 0)
        serializer = PhysicalInventorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def get_physical_inventories(self, request):
        physical_inventories = self.get_queryset()
        serializer = PhysicalInventorySerializer(physical_inventories, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def update_physical_inventory(self, request, pk=None):
        try:
            physical_inventory = self.get_object()
            data = request.data.copy()
            data['difference'] = data.get('counted_quantity', physical_inventory.counted_quantity) - data.get('on_hand_quantity', physical_inventory.on_hand_quantity)
            serializer = PhysicalInventorySerializer(physical_inventory, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f"Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['delete'])
    def delete_physical_inventory(self, request, pk=None):
        try:
            physical_inventory = self.get_object()
            physical_inventory.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"message": f"Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ScrapViewSet(viewsets.ModelViewSet):
    serializer_class = ScrapSerializer

    def get_queryset(self):
        user = self.request.user
        return Scrap.objects.filter(company=user.company)

    @action(detail=False, methods=['post'])
    def create_scrap(self, request):
        data = request.data.copy()
        data['company'] = request.user.company_id
        serializer = ScrapSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def get_scraps(self, request):
        scraps = self.get_queryset()
        serializer = ScrapSerializer(scraps, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def update_scrap(self, request, pk=None):
        try:
            scrap = self.get_object()
            data = request.data.copy()
            serializer = ScrapSerializer(scrap, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f"Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['delete'])
    def delete_scrap(self, request, pk=None):
        try:
            scrap = self.get_object()
            scrap.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"message": f"Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class LandedCostViewSet(viewsets.ModelViewSet):
    serializer_class = LandedCostSerializer

    def get_queryset(self):
        user = self.request.user
        return LandedCost.objects.filter(company=user.company)

    @action(detail=False, methods=['post'])
    def create_landed_cost(self, request):
        data = request.data.copy()
        data['company'] = request.user.company_id
        serializer = LandedCostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def get_landed_costs(self, request):
        landed_costs = self.get_queryset()
        serializer = LandedCostSerializer(landed_costs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def update_landed_cost(self, request, pk=None):
        try:
            landed_cost = self.get_object()
            data = request.data.copy()
            serializer = LandedCostSerializer(landed_cost, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f"Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['delete'])
    def delete_landed_cost(self, request, pk=None):
        try:
            landed_cost = self.get_object()
            landed_cost.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"message": f"Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductAttributeViewSet(viewsets.ModelViewSet):
    serializer_class = ProductAttributeSerializer

    def get_queryset(self):
        user = self.request.user
        return ProductAttribute.objects.filter(product__company=user.company)

    @action(detail=False, methods=['post'])
    def create_product_attribute(self, request):
        try:
            data = request.data.copy()
            data['company_id'] = str(request.user.company_id)
            serializer = ProductAttributeSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'])
    def get_product_attributes(self, request):
        attributes = self.get_queryset()
        serializer = ProductAttributeSerializer(attributes, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def update_product_attribute(self, request, pk=None):
        try:
            product_attribute = self.get_object()
            data = request.data.copy()
            serializer = ProductAttributeSerializer(product_attribute, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['delete'])
    def delete_product_attribute(self, request, pk=None):
        try:
            product_attribute = self.get_object()
            product_attribute.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"message": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UnitOfMeasureCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = UnitOfMeasureCategorySerializer

    def get_queryset(self):
        user = self.request.user
        return UnitOfMeasureCategory.objects.filter(company=user.company)

    @action(detail=False, methods=['post'])
    def create_unit_of_measure_category(self, request):
        try:
            data = request.data.copy()
            data['company_id'] = str(request.user.company_id)
            serializer = UnitOfMeasureCategorySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'])
    def get_unit_of_measure_categories(self, request):
        categories = self.get_queryset()
        serializer = UnitOfMeasureCategorySerializer(categories, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def update_unit_of_measure_category(self, request, pk=None):
        try:
            unit_of_measure_category = self.get_object()
            data = request.data.copy()
            serializer = UnitOfMeasureCategorySerializer(unit_of_measure_category, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['delete'])
    def delete_unit_of_measure_category(self, request, pk=None):
        try:
            unit_of_measure_category = self.get_object()
            unit_of_measure_category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"message": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductPackagingViewSet(viewsets.ModelViewSet):
    serializer_class = ProductPackagingSerializer

    def get_queryset(self):
        user = self.request.user
        return ProductPackaging.objects.filter(product__company=user.company)

    @action(detail=False, methods=['post'])
    def create_product_packaging(self, request):
        try:
            data = request.data.copy()
            data['company'] = str(request.user.company_id)
            serializer = ProductPackagingSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'])
    def get_product_packaging(self, request):
        packaging = self.get_queryset()
        serializer = ProductPackagingSerializer(packaging, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def update_product_packaging(self, request, pk=None):
        try:
            product_packaging = self.get_object()
            data = request.data.copy()
            serializer = ProductPackagingSerializer(product_packaging, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['delete'])
    def delete_product_packaging(self, request, pk=None):
        try:
            product_packaging = self.get_object()
            product_packaging.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"message": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ReorderingRuleViewSet(viewsets.ModelViewSet):
    serializer_class = ReorderingRuleSerializer

    def decode_jwt(self, token):
        try:
            access_token = AccessToken(token)
            return access_token
        except Exception as e:
            raise ValueError(f"Error decoding token: {str(e)}")

    def get_queryset(self):
        user = self.request.user
        return ReorderingRule.objects.filter(product__company=user.company)

    @action(detail=False, methods=['post'])
    def create_reordering_rule(self, request):
        try:
            token = request.COOKIES.get('jwt')
            if not token:
                return Response({"message": "JWT token not found in cookies"}, status=status.HTTP_400_BAD_REQUEST)

            decoded_token = self.decode_jwt(token)
            company_id = decoded_token.get('company_id')
            if not company_id:
                return Response({"message": "Company ID not found in token"}, status=status.HTTP_400_BAD_REQUEST)

            try:
                company_id = str(uuid.UUID(company_id))
            except ValueError as e:
                return Response({"message": f"Invalid company_id format: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

            try:
                company = Company.objects.get(id=company_id)
            except Company.DoesNotExist:
                return Response({"message": "Company not found"}, status=status.HTTP_404_NOT_FOUND)

            data = request.data
            data['company'] = company_id
            serializer = ReorderingRuleSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'])
    def get_reordering_rules(self, request):
        rules = self.get_queryset()
        serializer = ReorderingRuleSerializer(rules, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def update_reordering_rule(self, request, pk=None):
        try:
            reordering_rule = self.get_object()
            data = request.data.copy()
            serializer = ReorderingRuleSerializer(reordering_rule, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['delete'])
    def delete_reordering_rule(self, request, pk=None):
        try:
            reordering_rule = self.get_object()
            reordering_rule.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"message": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BarcodeNomenclatureViewSet(viewsets.ModelViewSet):
    serializer_class = BarcodeNomenclatureSerializer

    def decode_jwt(self, token):
        try:
            access_token = AccessToken(token)
            return access_token
        except Exception as e:
            raise ValueError(f"Error decoding token: {str(e)}")

    def get_queryset(self):
        user = self.request.user
        return BarcodeNomenclature.objects.filter(company=user.company)

    @action(detail=False, methods=['post'])
    def create_barcode_nomenclature(self, request):
        try:
            token = request.COOKIES.get('jwt')
            if not token:
                return Response({"message": "JWT token not found in cookies"}, status=status.HTTP_400_BAD_REQUEST)

            decoded_token = self.decode_jwt(token)
            company_id = decoded_token.get('company_id')
            if not company_id:
                return Response({"message": "Company ID not found in token"}, status=status.HTTP_400_BAD_REQUEST)

            try:
                company_id = str(uuid.UUID(company_id))
            except ValueError as e:
                return Response({"message": f"Invalid company_id format: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

            try:
                company = Company.objects.get(id=company_id)
            except company.DoesNotExist:
                return Response({"message": "Company not found"}, status=status.HTTP_404_NOT_FOUND)

            data = request.data
            data['company'] = company_id
            serializer = BarcodeNomenclatureSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'])
    def get_barcode_nomenclatures(self, request):
        nomenclatures = self.get_queryset()
        serializer = BarcodeNomenclatureSerializer(nomenclatures, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def update_barcode_nomenclature(self, request, pk=None):
        try:
            barcode_nomenclature = self.get_object()
            data = request.data.copy()
            serializer = BarcodeNomenclatureSerializer(barcode_nomenclature, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['delete'])
    def delete_barcode_nomenclature(self, request, pk=None):
        try:
            barcode_nomenclature = self.get_object()
            barcode_nomenclature.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"message": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)