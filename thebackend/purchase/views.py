import uuid

import jwt
from django.http import HttpResponse
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from weasyprint import HTML

from Authorisation.models import Company
from .models import Vendor, RequestForQuotation, PurchaseOrder, VendorPriceList
from .serializers import VendorSerializer, RequestForQuotationSerializer, PurchaseOrderSerializer, \
    VendorCreateSerializer, VendorPriceListSerializer
import logging

logger = logging.getLogger(__name__)


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    @action(detail=False, methods=['post'])
    def get_vendors(self, request):
        try:
            company_id = request.data.get('company_id')
            vendors = Vendor.objects.filter(vendor_company=company_id)
            serialized_vendors = []

            for vendor in vendors:
                serialized_vendor = {
                    'id': vendor.id,
                    'contact_country': vendor.contact_country,
                    'tax_id': vendor.tax_id,
                    'email': vendor.email
                }

                if vendor.type == 'individual':
                    serialized_vendor['name'] = vendor.name
                    serialized_vendor['mobile'] = vendor.mobile
                elif vendor.type == 'company':
                    serialized_vendor['company_name'] = vendor.company_name
                    serialized_vendor['phone'] = vendor.phone

                serialized_vendors.append(serialized_vendor)

            return Response(serialized_vendors)

        except Exception as e:
            return Response({"message": f"Error {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['post'])
    def create_vendor(self, request):
        try:
            serializer = VendorCreateSerializer(data=request.data)
            print(f"this is the data sent from frontend{serializer}")
            if serializer.is_valid():
                vendor_data = serializer.validated_data
                vendor_type = vendor_data['type']
                company_id = vendor_data['vendor_company']

                if vendor_type == 'individual':
                    existing_vendor = Vendor.objects.filter(
                        type='individual',
                        name=vendor_data['name'],
                        vendor_company=company_id
                    ).exists()
                elif vendor_type == 'company':
                    existing_vendor = Vendor.objects.filter(
                        type='company',
                        company_name=vendor_data['company_name'],
                        vendor_company=company_id
                    ).exists()

                if existing_vendor:
                    return Response(
                        {"message": "Vendor already exists"},
                        status=status.HTTP_400_BAD_REQUEST
                    )

                serializer.save()
                return Response({"message": "Vendor successfully created"}, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f"Error {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RequestForQuotationViewSet(viewsets.ModelViewSet):
    queryset = RequestForQuotation.objects.all()
    serializer_class = RequestForQuotationSerializer

    def generate_reference(prefix, model):
        year = timezone.now().year
        month = timezone.now().month
        count = model.objects.filter(created_at__year=year, created_at__month=month).count() + 1
        return f"{prefix}/{year}/{month:02d}/{count:04d}"

    # RFQ creation method
    @action(detail=False, methods=['post'])
    @permission_classes([IsAuthenticated])
    def create_rfq(self, request):
        try:
            data = request.data
            data['company'] = request.user.company.id
            data['buyer'] = request.user.id
            data['reference'] = self.generate_reference('RFQ', RequestForQuotation)
            serializer = RequestForQuotationSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error creating RFQ: {e}", exc_info=True)
            return Response({'detail': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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

        # Include company logo if available
        if hasattr(rfq.company, 'logo') and rfq.company.logo.image:
            logo_path = rfq.company.logo.image.path
            p.drawImage(logo_path, 400, 750, width=100, height=50)

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
            logger.error(f"Error sending email for RFQ {rfq.reference}: {e}")
            return False


class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def generate_reference(prefix, model):
        year = timezone.now().year
        month = timezone.now().month
        count = model.objects.filter(created_at__year=year, created_at__month=month).count() + 1
        return f"{prefix}/{year}/{month:02d}/{count:04d}"

    @action(detail=False, methods=['post'])
    def create_po(self, request):
        try:
            data = request.data
            data['company'] = request.user.company.id
            data['buyer'] = request.user.id
            data['reference'] = self.generate_reference('PO', PurchaseOrder)
            serializer = PurchaseOrderSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error creating PO: {e}")
            return Response({'detail': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'])
    def get_pos(self, request):
        pos = self.get_queryset().filter(company=request.user.company)
        serializer = PurchaseOrderSerializer(pos, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def print_po(self, request, pk=None):
        po = self.get_object()
        company = request.user.company
        html_string = render_to_string('purchase_order.html', {
            'po': po,
            'company_name': company.name,
            'company_address': company.address,
            'company_phone': company.phone,
            'company_email': company.email,
            'company_website': company.website,
            'company_logo': company.logo.image.url if hasattr(company, 'logo') else '',
            'company_footer': company.footer,
        })
        pdf_file = HTML(string=html_string).write_pdf()

        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="PO_{po.reference}.pdf"'
        return response

    @action(detail=True, methods=['post'])
    def email_po(self, request, pk=None):
        po = self.get_object()
        company = request.user.company
        html_string = render_to_string('purchase_order.html', {
            'po': po,
            'company_name': company.name,
            'company_address': company.address,
            'company_phone': company.phone,
            'company_email': company.email,
            'company_website': company.website,
            'company_logo': company.logo.image.url if hasattr(company, 'logo') else '',
            'company_footer': company.footer,
        })
        pdf_file = HTML(string=html_string).write_pdf()

        subject = f"Purchase Order: {po.reference}"
        body = f"Dear {po.vendor.company_name},\n\nPlease find attached the Purchase Order.\n\nBest regards,\n{company.name}"
        email = EmailMessage(subject, body, settings.DEFAULT_FROM_EMAIL, [po.vendor.email])
        email.attach(f"PO_{po.reference}.pdf", pdf_file, 'application/pdf')
        try:
            email.send()
            return Response({'status': 'email sent'}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error sending email for PO {po.reference}: {e}")
            return Response({'status': 'email failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def _generate_pdf(self, po, return_as_file=False):
        buffer = BytesIO()
        p = canvas.Canvas(buffer)

        # Include company logo if available
        if hasattr(po.company, 'logo') and po.company.logo.image:
            logo_path = po.company.logo.image.path
            p.drawImage(logo_path, 400, 750, width=100, height=50)

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
            logger.error(f"Error sending email for PO {po.reference}: {e}")
            return False


class VendorPriceListViewSet(viewsets.ModelViewSet):
    serializer_class = VendorPriceListSerializer

    def get_queryset(self):
        user = self.request.user
        return VendorPriceList.objects.filter(product__company=user.company)

    @action(detail=False, methods=['post'])
    def create_vendor_price_list(self, request):
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
            data['company_id'] = company_id
            serializer = VendorPriceListSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'])
    def get_vendor_price_lists(self, request):
        price_lists = self.get_queryset()
        serializer = VendorPriceListSerializer(price_lists, many=True)
        return Response(serializer.data)
