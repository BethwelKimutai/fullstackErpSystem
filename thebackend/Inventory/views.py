from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from Authorisation.models import Company
from .models import Product, Receipt, Delivery, InternalTransfer, PhysicalInventory, Scrap, LandedCost
from .serializers import (ProductSerializer, ReceiptSerializer, DeliverySerializer,
                          InternalTransferSerializer, PhysicalInventorySerializer,
                          ScrapSerializer, LandedCostSerializer)


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
        data = request.data
        data['company'] = request.user.company.id
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def get_products(self, request):
        products = self.get_queryset()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def replenish(self, request):
        data = request.data
        data['company'] = request.user.company.id
        data['user'] = request.user.id
        serializer = ReplenishOrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def purchase(self, request):
        data = request.data
        data['company'] = request.user.company.id
        data['user'] = request.user.id
        serializer = PurchaseOrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get', 'post'])
    def inventory(self, request):
        if request.method == 'POST':
            data = request.data
            data['company'] = request.user.company.id
            data['user'] = request.user.id
            serializer = InventorySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            inventories = Inventory.objects.filter(company=request.user.company)
            serializer = InventorySerializer(inventories, many=True)
            return Response(serializer.data)


class ReceiptViewSet(viewsets.ModelViewSet):
    serializer_class = ReceiptSerializer

    def get_queryset(self):
        user = self.request.user
        return Receipt.objects.filter(company=user.company)

    @action(detail=False, methods=['post'])
    def create_receipt(self, request):
        data = request.data
        data['company'] = request.user.company.id
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


class DeliveryViewSet(viewsets.ModelViewSet):
    serializer_class = DeliverySerializer

    def get_queryset(self):
        user = self.request.user
        return Delivery.objects.filter(company=user.company)

    @action(detail=False, methods=['post'])
    def create_delivery(self, request):
        data = request.data
        data['company'] = request.user.company.id
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


class InternalTransferViewSet(viewsets.ModelViewSet):
    serializer_class = InternalTransferSerializer

    def get_queryset(self):
        user = self.request.user
        return InternalTransfer.objects.filter(company=user.company)

    @action(detail=False, methods=['post'])
    def create_internal_transfer(self, request):
        data = request.data
        data['company'] = request.user.company.id
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


class PhysicalInventoryViewSet(viewsets.ModelViewSet):
    serializer_class = PhysicalInventorySerializer

    def get_queryset(self):
        user = self.request.user
        return PhysicalInventory.objects.filter(company=user.company)

    @action(detail=False, methods=['post'])
    def create_physical_inventory(self, request):
        data = request.data
        data['company'] = request.user.company.id
        data['user'] = request.user.id
        data['difference'] = data['counted_quantity'] - data['on_hand_quantity']
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


class ScrapViewSet(viewsets.ModelViewSet):
    serializer_class = ScrapSerializer

    def get_queryset(self):
        user = self.request.user
        return Scrap.objects.filter(company=user.company)

    @action(detail=False, methods=['post'])
    def create_scrap(self, request):
        data = request.data
        data['company'] = request.user.company.id
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


class LandedCostViewSet(viewsets.ModelViewSet):
    serializer_class = LandedCostSerializer

    def get_queryset(self):
        user = self.request.user
        return LandedCost.objects.filter(company=user.company)

    @action(detail=False, methods=['post'])
    def create_landed_cost(self, request):
        data = request.data
        data['company'] = request.user.company.id
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
