import token

import jwt
import random
import string
import uuid
from datetime import datetime, timedelta
import timedelta

import phonenumbers
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.messages.storage import session
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.serializers import json
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from phonenumbers.phonenumberutil import parse, format_number, region_code_for_number
from pycountry import countries

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from thebackend import settings
from .models import Company, User, UserOTP
from .serializers import (
    CompanySerializer, UserSerializer, UserDetailsSerializer, PasswordChangeSerializer,
    UserAvatarSerializer, CompanyLogoSerializer, UserLoginSerializer
)
from .utils import generate_jwt, decode_jwt

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
            serializer = self.get_serializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            duplicate_exists = Company.objects.filter(email=request.data['email']).exists()
            if duplicate_exists and request.data.get('is_approved', False):
                return Response({'error': 'Company already approved.'}, status=status.HTTP_400_BAD_REQUEST)

            phone_number = request.data.get('phone_number')
            if phone_number:
                try:
                    parsed_number = parse(phone_number)
                    self.instance.country_code = f"+{parsed_number.country_code}"
                    self.instance.number = format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)

                    country_code = region_code_for_number(parsed_number)
                    country = countries.get(alpha_2=country_code)
                    if country:
                        self.instance.country = country.name
                except phonenumbers.phonenumberutil.NumberParseException as e:
                    raise ValidationError(f"Invalid phone number: {e}")

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

            admin_user = User.objects.create(
                username=f"{company.email.split('@')[0]}-{random.randint(1000, 9999)}",
                email=company.email,
                company=company,
                is_manager=True,
                is_superuser=False,
                is_staff=True
            )
            admin_user.set_password('jikoTrack@2024')
            admin_user.save()

            send_mail(
                'Registration Approved',
                f"""Your registration has been approved. Here are your admin credentials:
                    \nUsername: {admin_user.username}\nPassword: jikoTrack@2024.
                    \n We advise you change your password immediately because of security reasons. 
                    This password expires after 24 hours""",
                'from@example.com',
                [company.email],
                fail_silently=False,
            )

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

    @action(detail=True, methods=['post'])
    def upload_company_logo(self, request, pk=id):
        try:
            try:
                company_id = uuid.UUID(pk)
            except ValueError:
                return Response({'error': 'Invalid UUID'}, status=status.HTTP_400_BAD_REQUEST)

            company = Company.objects.get(id=company_id)
            if not request.user.is_superuser and request.user != company.user:
                return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

            serializer = CompanyLogoSerializer(company, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Company.DoesNotExist:
            return Response({'error': 'Company not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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

            jwt_token = generate_jwt(user)

            user_details = {
                'id': str(user.id),
                'username': user.username,
                'email': user.email,
                'is_manager': user.is_manager,
                'is_accounting_manager': user.is_accounting_manager,
                'is_inventory_manager': user.is_inventory_manager,
                'is_purchase_manager': user.is_purchase_manager,
                'is_superuser': user.is_superuser,
                'company_id': str(user.company_id) if user.company_id else None
            }

            response_data = {
                'access': jwt_token,
                'user_details': user_details
            }

            request.session['jwt_token'] = jwt_token

            serializer = UserLoginSerializer(data=response_data)
            if serializer.is_valid():
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def logout(self, request):
        try:
            request.session.flush()
            logout(request)
            return Response({'message': 'User logged out successfully'})
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def getUsers(self, request):
        try:
            sessionid = request.session.get(session)
            for sessions in sessionid:
                token = request.session.get('jwt_token')
                if not token:
                    return Response({"message": "User is not authenticated."}, status=status.HTTP_401_UNAUTHORIZED)

            user = self.decode_jwt(token)
            if not user:
                return Response({"message": "User is not authenticated."}, status=status.HTTP_401_UNAUTHORIZED)

            return Response(user, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def createUser(self, request):
        try:
            role_mapping = {
                'Manager': 'is_manager',
                'Admin': 'is_staff',
                'Accounting Manager': 'is_accounting_manager',
                'Inventory Manager': 'is_inventory_manager',
                'Purchase Manager': 'is_purchase_manager',
                'User': None
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
                    f"Thank you for creating an account with our app!\n\n"
                    f"You can now log in using your username: {user.username}\n"
                    f"For security reasons, your password is not included in this email.\n"
                    f"Please visit the login page to set your password.\n\n"
                    f"We hope you enjoy using our app!\n\nSincerely,\nJikoTrack Team",
                    'from@example.com',
                    [user.email],
                    fail_silently=False,
                )

                return Response({'status': 'user created'}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
    def sign_out(self, request):
        try:
            token = request.headers.get('Authorization', '').split(' ')[1]
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
                'user_id': str(user.id),
                'login_time': login_time.isoformat()
            }

            response = Response()
            response.set_cookie(key='temp_session', value=json.dumps(temp_session), httponly=True)
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
                temp_session = json.loads(temp_session)
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

            refresh = RefreshToken.for_user(user)

            login(request, user)

            response = Response()
            response.set_cookie(key='jwt', value=str(refresh.access_token), httponly=True)
            response.delete_cookie('temp_session')
            response.data = {
                'message': 'User signed in successfully and session resumed',
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }

            return response

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def getAllUsers(self, request):
        try:
            users = User.objects.all().select_related('company')
            user_list = []

            for user in users:
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
                    'company_name': user.company.name if user.company else None
                }
                user_list.append(user_details)

            return Response(user_list, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def newPassword(self, request):
        try:
            new_password = request.data.get('new_password')
            confirm_password = request.data.get('confirm_password')

            if not new_password or not confirm_password:
                raise ValidationError('Both new password and confirm password are required.')

            if new_password != confirm_password:
                raise ValidationError('Passwords do not match.')

            username_or_email = request.data.get('username') or request.data.get('email')
            if not username_or_email:
                raise ValidationError('Username or email is required.')

            user = User.objects.filter(Q(username=username_or_email) | Q(email=username_or_email)).first()
            if not user:
                return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

            user.password = make_password(new_password)
            user.save()

            return Response({'message': 'Password updated successfully.'}, status=status.HTTP_200_OK)
        except ValidationError as ve:
            return Response({'message': str(ve)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def forgotPasswordOtpVerification(self, request):
        try:
            otp = request.data.get('otp')
            if not otp:
                return Response({'message': 'OTP is required'}, status=status.HTTP_400_BAD_REQUEST)

            user_otp = UserOTP.objects.filter(otp=otp).first()

            if not user_otp:
                return Response({'message': 'User not found or OTP is incorrect'}, status=status.HTTP_404_NOT_FOUND)

            otp_age = timezone.now() - user_otp.created_at
            if otp_age.total_seconds() > 600:
                return Response({'message': 'OTP has expired'}, status=status.HTTP_400_BAD_REQUEST)

            user = user_otp.user
            user.is_active = True
            user.save()

            user_otp.delete()

            return Response({'message': 'Account verified successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def forgotPassword(self, request):
        try:
            username_or_email = request.data.get('username') or request.data.get('email')
            if not username_or_email:
                raise ValidationError('Username or email is required')

            user = User.objects.filter(Q(username=username_or_email) | Q(email=username_or_email)).first()
            if not user:
                return Response({'status': 'user not found'}, status=status.HTTP_404_NOT_FOUND)

            otp = ''.join(random.choices(string.digits, k=6))

            user_otp, created = UserOTP.objects.get_or_create(user=user)
            user_otp.otp = otp
            user_otp.created_at = timezone.now()
            user_otp.save()

            send_mail(
                'Password Reset Request',
                f'Your one-time password (OTP) to reset your password is: {otp}',
                'from@example.com',
                [user.email],
                fail_silently=False,
            )

            return Response({'status': 'otp sent'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def roles(self, request):
        roles = [
            {"name": "Manager"},
            {"name": "Accounting Manager"},
            {"name": "Inventory Manager"},
            {"name": "Purchase Manager"},
        ]
        return Response(roles, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def change_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordChangeSerializer(data=request.data)
        if serializer.is_valid():
            if not check_password(serializer.validated_data['current_password'], user.password):
                return Response({"detail": "Current password is incorrect"}, status=status.HTTP_400_BAD_REQUEST)
            user.password = make_password(serializer.validated_data['new_password'])
            user.save()
            send_mail(
                'Password Changed',
                'Your password has been changed successfully.',
                'from@example.com',
                [user.email],
                fail_silently=False,
            )
            return Response({"detail": "Password updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def update_user_info(self, request):
        token = request.headers.get('Authorization', '').split(' ')[1]

        try:
            access_token = AccessToken(token)
            user_id = access_token['user_id']
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        user = get_object_or_404(User, pk=user_id)

        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def upload_user_avatar(self, request, pk=None):
        user = request.user

        if not user.is_authenticated:
            return Response({'detail': 'Authentication credentials were not provided.'},
                            status=status.HTTP_401_UNAUTHORIZED)

        serializer = UserAvatarSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
