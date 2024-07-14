from django.urls import path
from .views import VendorViewSet, RequestForQuotationViewSet, PurchaseOrderViewSet, VendorPriceListViewSet

urlpatterns = [
    path('vendors/createvendors/', VendorViewSet.as_view({'post':'create_vendor'}), name='vendors'),
    path('vendors/getvendors/', VendorViewSet.as_view({'post':'get_vendors'}), name='vendor-detail'),
    path('rfqs/create/', RequestForQuotationViewSet.as_view({'post': 'create_rfq'}), name='create-rfq'),
    path('rfqs/', RequestForQuotationViewSet.as_view({'get': 'get_rfqs'}), name='get-rfqs'),
    path('rfqs/<int:pk>/print/', RequestForQuotationViewSet.as_view({'get': 'print_rfq'}), name='print-rfq'),
    path('rfqs/<int:pk>/email/', RequestForQuotationViewSet.as_view({'post': 'email_rfq'}), name='email-rfq'),
    path('pos/create/', PurchaseOrderViewSet.as_view({'post': 'create_po'}), name='create-po'),
    path('pos/', PurchaseOrderViewSet.as_view({'get': 'get_pos'}), name='get-pos'),
    path('pos/<int:pk>/print/', PurchaseOrderViewSet.as_view({'get': 'print_po'}), name='print-po'),
    path('pos/<int:pk>/email/', PurchaseOrderViewSet.as_view({'post': 'email_po'}), name='email-po'),
    path('vendorpl/create/', VendorPriceListViewSet.as_view({'post': 'create_vendor_price_list'}), name='create-vendor-price-list'),
    path('vendorpl/get/', VendorPriceListViewSet.as_view({'get': 'get_vendor_price_lists'}), name='get-vendor-price-list'),
]
