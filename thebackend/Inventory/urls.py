from django.urls import path, include
from .views import (ProductViewSet, ReceiptViewSet, DeliveryViewSet, InternalTransferViewSet,
                    PhysicalInventoryViewSet, ScrapViewSet, LandedCostViewSet)

urlpatterns = [
    path('products/create/', ProductViewSet.as_view({'post': 'create_product'}), name='create-product'),
    path('products/', ProductViewSet.as_view({'get': 'get_products'}), name='get-products'),
    path('products/replenish/', ProductViewSet.as_view({'post': 'replenish'}), name='replenish-order'),
    path('products/purchase/', ProductViewSet.as_view({'post': 'purchase'}), name='purchase-order'),
    path('products/inventory/', ProductViewSet.as_view({'get': 'inventory', 'post': 'inventory'}), name='inventory'),
    path('receipts/create/', ReceiptViewSet.as_view({'post': 'create_receipt'}), name='create-receipt'),
    path('receipts/', ReceiptViewSet.as_view({'get': 'get_receipts'}), name='get-receipts'),
    path('deliveries/create/', DeliveryViewSet.as_view({'post': 'create_delivery'}), name='create-delivery'),
    path('deliveries/', DeliveryViewSet.as_view({'get': 'get_deliveries'}), name='get-deliveries'),
    path('internal-transfers/create/', InternalTransferViewSet.as_view({'post': 'create_internal_transfer'}), name='create-internal-transfer'),
    path('internal-transfers/', InternalTransferViewSet.as_view({'get': 'get_internal_transfers'}), name='get-internal-transfers'),
    path('physical-inventory/create/', PhysicalInventoryViewSet.as_view({'post': 'create_physical_inventory'}), name='create-physical-inventory'),
    path('physical-inventory/', PhysicalInventoryViewSet.as_view({'get': 'get_physical_inventories'}), name='get-physical-inventories'),
    path('scrap/create/', ScrapViewSet.as_view({'post': 'create_scrap'}), name='create-scrap'),
    path('scrap/', ScrapViewSet.as_view({'get': 'get_scraps'}), name='get-scraps'),
    path('landed-costs/create/', LandedCostViewSet.as_view({'post': 'create_landed_cost'}), name='create-landed-cost'),
    path('landed-costs/', LandedCostViewSet.as_view({'get': 'get_landed_costs'}), name='get-landed-costs'),
]