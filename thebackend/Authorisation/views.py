import random
from datetime import datetime, timedelta

import phonenumbers
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from pip._internal.utils import logging
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import AuthenticationFailed, NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.utils import json
from simplejwt import jwt

from .models import Company, User, UserOTP
from .serializers import CompanySerializer, UserSerializer, UserDetailsSerializer
from django.core.exceptions import ValidationError
from phonenumbers import parse, format_number, region_code_for_number
from pycountry import countries
import jwt
import datetime

User = get_user_model()


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.instance = None

    @action(detail=False, methods=['post'])
    def register(self, request):
        try:
            # 1. Field Validation with Custom Serializer
            serializer = self.get_serializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # 2. Duplicate Check
            duplicate_exists = Company.objects.filter(email=request.data['email']).exists()
            if duplicate_exists and request.data.get('is_approved', False):
                return Response({'error': 'Company already approved.'}, status=status.HTTP_400_BAD_REQUEST)
            elif duplicate_exists:
                # Allow multiple registrations for non-approved companies
                pass

            # 3. Extract Country Code and Name from Phone Number (if applicable)
            phone_number = request.data.get('phone_number')
            if phone_number:
                try:
                    parsed_number = parse(phone_number)
                    self.instance.country_code = f"+{parsed_number.country_code}"
                    self.instance.number = format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)

                    # Get country name from country code
                    country_code = region_code_for_number(parsed_number)
                    country = countries.get(alpha_2=country_code)
                    if country:
                        self.instance.country = country.name
                except phonenumbers.phonenumberutil.NumberParseException as e:
                    raise ValidationError(f"Invalid phone number: {e}")

            # 4. Save with Conditional Approval and Email Notification
            self.instance = serializer.save(is_approved=False)
            send_mail(
                'Registration Request Received',
                'Your registration request has been received and is awaiting approval.',
                'from@example.com',
                [self.instance.email],
                fail_silently=False,
            )

            return Response({'status': 'pending approval'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        try:
            company = self.get_object()
            if company.is_approved:
                return Response({"message": "Company already approved"}, status=status.HTTP_400_BAD_REQUEST)

            # Create an admin user for the approved company
            admin_user = User.objects.create(
                username=f"{company.email.split('@')[0]}-{random.randint(1000, 9999)}",
                email=company.email,
                company=company,
                password=f"{random.randint(100000, 999999)}",
                is_manager=True,
                is_superuser=False,
                is_staff=True
            )
            admin_user.set_password('jikoTrack@2024')
            admin_user.save()

            send_mail(
                'Registration Approved',
                f"""Your registration has been approved. Here are your admin credentials:\n\nUsername: {admin_user.username}\nPassword: jikoTrack@2024""",
                'from@example.com',
                [company.email],
                fail_silently=False,
            )

            # Update the company's approval status after email is sent
            company.is_approved = True
            company.save()

            return Response({'status': 'approved'})
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def companiesList(self, request):
        companies = Company.objects.filter(is_approved=True)
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    methods = ['get']

    def getAllCompanies(self, request):
        try:
            companies = Company.objects.all()
            company_list = []

            for company in companies:
                company_details = {
                    'id': company.id,
                    'name': company.companyName,
                    'email': company.email,
                    'country': company.country,
                    'city': company.city,
                    'companySize': company.companySize,
                    'primaryInterest': company.primaryInterest,
                    'is_approved': company.is_approved,
                }
                company_list.append(company_details)

            return Response(company_list, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):
        try:
            username = request.data.get('username').lower()
            password = request.data.get('password')

            user = authenticate(username=username, password=password)
            if not user:
                return Response({"message": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)

            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
                'iat': datetime.datetime.utcnow(),
                'sub': user.id
            }

            token = jwt.encode(payload, 'secret', algorithm='HS256')
            company = Company.objects.get(id=user.company_id)
            user_details = {
                'token': token,
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'company_name': company.companyName,
                'is_manager': user.is_manager,
                'is_accounting_manager': user.is_accounting_manager,
                'is_inventory_manager': user.is_inventory_manager,
                'is_purchase_manager': user.is_purchase_manager,
                'is_superuser': user.is_superuser
            }

            response = Response()
            response.set_cookie(key='jwt', value=token, httponly=True)
            response.data = {
                'jwt': token,
                'user_details': user_details
            }

            return response

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def createUser(self, request):
        try:
            # Convert roles from word form to the form understood by the serializer
            role_mapping = {
                'Manager': 'is_manager',
                'Admin': 'is_staff',
                'Accounting Manager': 'is_accounting_manager',
                'Inventory Manager': 'is_inventory_manager',
                'Purchase Manager': 'is_purchase_manager',
                'User': None  # No specific role for 'User'
            }

            role = request.data.get('role')
            if role:
                role_field = role_mapping.get(role)
                if role_field is not None:
                    request.data[role_field] = True

            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()

                send_mail(
                    'Welcome to JikoTrack!',
                    f"""
                        Thank you for creating an account with our app!

                        You can now log in using your username: {user.username}

                        For security reasons, your password is not included in this email.
                        Please visit the login page to set your password.

                        We hope you enjoy using our app!

                        Sincerely,
                        JikoTrack Team
                        """,
                    'from@example.com',
                    [user.email],
                    fail_silently=False,
                )

                return Response({'status': 'user created'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def getUsers(self, request):
        try:
            # Get the JWT token from the cookies
            token = request.COOKIES.get('jwt')

            if not token:
                return Response({"message": "Unauthenticated"}, status=status.HTTP_401_UNAUTHORIZED)

            # Decode the JWT token
            try:
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            except jwt.ExpiredSignatureError:
                return Response({"message": "Authentication token has expired"}, status=status.HTTP_401_UNAUTHORIZED)
            except jwt.InvalidTokenError:
                return Response({"message": "Invalid authentication token"}, status=status.HTTP_401_UNAUTHORIZED)

            # Get the user ID from the payload
            user_id = payload.get('sub')
            if not user_id:
                return Response({"message": "Invalid payload in token"}, status=status.HTTP_401_UNAUTHORIZED)

            # Retrieve the user object
            user = get_object_or_404(User, id=user_id)

            # Serialize the logged-in user data
            serializer = UserDetailsSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def deleteUser(self, request, pk=None):
        try:
            user = self.get_object()

            if user.is_superuser:
                return Response({"message": "Cannot delete superuser"}, status=status.HTTP_400_BAD_REQUEST)

            user.delete()

            return Response({'status': 'user deleted'})
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def logout(self, request):
        try:
            response = Response()
            response.delete_cookie('jwt')
            logout(request)
            response.data = {'message': 'User logged out successfully'}
            return response
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def sign_out(self, request):
        try:
            token = request.COOKIES.get('jwt')

            if not token:
                return Response({"message": "Authentication token not provided"}, status=status.HTTP_401_UNAUTHORIZED)

            try:
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            except jwt.ExpiredSignatureError:
                return Response({"message": "Authentication token has expired"}, status=status.HTTP_401_UNAUTHORIZED)
            except jwt.InvalidTokenError:
                return Response({"message": "Invalid authentication token"}, status=status.HTTP_401_UNAUTHORIZED)

            user_id = payload['sub']
            user = get_object_or_404(User, id=user_id)

            login_time = timezone.now()

            temp_session = {
                'user_id': user.id,
                'login_time': login_time.isoformat()
            }

            response = Response()
            response.set_cookie(key='temp_session', value=json.dumps(temp_session),
                                httponly=True)  # JSON encode the session data
            response.delete_cookie('jwt')
            logout(request)
            response.data = {'message': 'User signed out temporarily'}
            return response
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def sign_in(self, request):
        try:
            temp_session = request.COOKIES.get('temp_session')

            if not temp_session:
                return Response({"message": "Temporary session not found"}, status=status.HTTP_400_BAD_REQUEST)

            try:
                temp_session = json.loads(temp_session)  # Decode the JSON-encoded string
            except:
                return Response({"message": "Invalid temporary session data"}, status=status.HTTP_400_BAD_REQUEST)

            password = request.data.get('password')
            if not password:
                return Response({"message": "Password not provided"}, status=status.HTTP_400_BAD_REQUEST)

            user_id = temp_session.get('user_id')
            login_time = temp_session.get('login_time')

            if not user_id or not login_time:
                return Response({"message": "Invalid temporary session data"}, status=status.HTTP_400_BAD_REQUEST)

            user = get_object_or_404(User, id=user_id)
            user = authenticate(username=user.username, password=password)

            if user is None:
                return Response({"message": "Invalid password"}, status=status.HTTP_401_UNAUTHORIZED)

            # Create JWT token
            payload = {
                'sub': user.id,
                'iat': timezone.now(),
                'exp': timezone.now() + timezone.timedelta(hours=1)
            }
            token = jwt.encode(payload, 'secret', algorithm='HS256')

            # Log the user in
            login(request, user)

            # Create response
            response = Response()
            response.set_cookie(key='jwt', value=token, httponly=True)
            response.delete_cookie('temp_session')
            response.data = {'message': 'User signed in successfully and session resumed'}

            return response

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def getAllUsers(self, request):
        try:
            users = User.objects.all().select_related('company')  # Optimize queries by selecting related company
            user_list = []

            for user in users:
                # Determine the role based on the hierarchy
                if user.is_superuser:
                    role = 'superuser'
                elif user.is_manager:
                    role = 'manager'
                elif user.is_accounting_manager:
                    role = 'accounting_manager'
                elif user.is_inventory_manager:
                    role = 'inventory_manager'
                elif user.is_purchase_manager:
                    role = 'purchase_manager'
                else:
                    role = 'user'

                user_details = {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'role': role,
                    'last_name': user.last_name,
                    'is_active': user.is_active,
                    'company_name': user.company.name if user.company else None  # Add company name
                }
                user_list.append(user_details)

            return Response(user_list, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
