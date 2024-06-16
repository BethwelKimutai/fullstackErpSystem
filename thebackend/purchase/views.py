from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from .models import Vendor, RequestForQuotation, PurchaseOrder
from .serializers import VendorSerializer, RequestForQuotationSerializer, PurchaseOrderSerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    @action(detail=False, methods=['post'])
    def create_vendor(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def get_vendors(self, request):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

class RequestForQuotationViewSet(viewsets.ModelViewSet):
    queryset = RequestForQuotation.objects.all()
    serializer_class = RequestForQuotationSerializer

    @action(detail=False, methods=['post'])
    def create_rfq(self, request):
        data = request.data
        data['company'] = request.user.company.id
        data['buyer'] = request.user.id
        serializer = RequestForQuotationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def get_rfqs(self, request):
        rfqs = self.get_queryset().filter(company=request.user.company)
        serializer = RequestForQuotationSerializer(rfqs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def print_rfq(self, request, pk=None):
        rfq = self.get_object()
        response = self._generate_pdf(rfq)
        return response

    @action(detail=True, methods=['post'])
    def email_rfq(self, request, pk=None):
        rfq = self.get_object()
        pdf_file = self._generate_pdf(rfq, return_as_file=True)
        email_sent = self._send_email(rfq, pdf_file)
        if email_sent:
            return Response({'status': 'email sent'}, status=status.HTTP_200_OK)
        return Response({'status': 'email failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def _generate_pdf(self, rfq, return_as_file=False):
        buffer = BytesIO()
        p = canvas.Canvas(buffer)
        p.drawString(100, 750, f"Request for Quotation: {rfq.reference}")
        p.drawString(100, 730, f"Vendor: {rfq.vendor.company_name}")
        p.drawString(100, 710, f"Product: {rfq.product.name}")
        p.drawString(100, 690, f"Total: {rfq.total}")
        p.showPage()
        p.save()
        buffer.seek(0)

        if return_as_file:
            return buffer

        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="RFQ_{rfq.reference}.pdf"'
        return response

    def _send_email(self, rfq, pdf_file):
        subject = f"Request for Quotation: {rfq.reference}"
        body = f"Dear {rfq.vendor.company_name},\n\nPlease find attached the Request for Quotation.\n\nBest regards,\n{rfq.company.name}"
        email = EmailMessage(subject, body, settings.DEFAULT_FROM_EMAIL, [rfq.vendor.email])
        email.attach(f"RFQ_{rfq.reference}.pdf", pdf_file.read(), 'application/pdf')
        try:
            email.send()
            return True
        except Exception as e:
            print(e)
            return False

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    @action(detail=False, methods=['post'])
    def create_po(self, request):
        data = request.data
        data['company'] = request.user.company.id
        data['buyer'] = request.user.id
        serializer = PurchaseOrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def get_pos(self, request):
        pos = self.get_queryset().filter(company=request.user.company)
        serializer = PurchaseOrderSerializer(pos, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def print_po(self, request, pk=None):
        po = self.get_object()
        response = self._generate_pdf(po)
        return response

    @action(detail=True, methods=['post'])
    def email_po(self, request, pk=None):
        po = self.get_object()
        pdf_file = self._generate_pdf(po, return_as_file=True)
        email_sent = self._send_email(po, pdf_file)
        if email_sent:
            return Response({'status': 'email sent'}, status=status.HTTP_200_OK)
        return Response({'status': 'email failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def _generate_pdf(self, po, return_as_file=False):
        buffer = BytesIO()
        p = canvas.Canvas(buffer)
        p.drawString(100, 750, f"Purchase Order: {po.reference}")
        p.drawString(100, 730, f"Vendor: {po.vendor.company_name}")
        p.drawString(100, 710, f"Product: {po.product.name}")
        p.drawString(100, 690, f"Total: {po.total}")
        p.showPage()
        p.save()
        buffer.seek(0)

        if return_as_file:
            return buffer

        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="PO_{po.reference}.pdf"'
        return response

    def _send_email(self, po, pdf_file):
        subject = f"Purchase Order: {po.reference}"
        body = f"Dear {po.vendor.company_name},\n\nPlease find attached the Purchase Order.\n\nBest regards,\n{po.company.name}"
        email = EmailMessage(subject, body, settings.DEFAULT_FROM_EMAIL, [po.vendor.email])
        email.attach(f"PO_{po.reference}.pdf", pdf_file.read(), 'application/pdf')
        try:
            email.send()
            return True
        except Exception as e:
            print(e)
            return False
