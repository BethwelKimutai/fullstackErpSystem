from django.urls import path
from .views import VendorViewSet, RequestForQuotationViewSet, PurchaseOrderViewSet

urlpatterns = [
    path('vendors/create/', vendorviewset.as_view({'post':'create_vendor'}), name='vendors'),
    path('vendors/get/', vendorviewset.as_view({'get':'get_vendors'}), name='vendor-detail'),
    path('rfqs/create/', RequestForQuotationViewSet.as_view({'post': 'create_rfq'}), name='create-rfq'),
    path('rfqs/', RequestForQuotationViewSet.as_view({'get': 'get_rfqs'}), name='get-rfqs'),
    path('rfqs/<int:pk>/print/', RequestForQuotationViewSet.as_view({'get': 'print_rfq'}), name='print-rfq'),
    path('rfqs/<int:pk>/email/', RequestForQuotationViewSet.as_view({'post': 'email_rfq'}), name='email-rfq'),
    path('pos/create/', PurchaseOrderViewSet.as_view({'post': 'create_po'}), name='create-po'),
    path('pos/', PurchaseOrderViewSet.as_view({'get': 'get_pos'}), name='get-pos'),
    path('pos/<int:pk>/print/', PurchaseOrderViewSet.as_view({'get': 'print_po'}), name='print-po'),
    path('pos/<int:pk>/email/', PurchaseOrderViewSet.as_view({'post': 'email_po'}), name='email-po'),
]
