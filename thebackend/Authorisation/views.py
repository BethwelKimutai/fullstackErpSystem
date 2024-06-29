import random
import string
from datetime import datetime, timedelta

import phonenumbers
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.handlers.modwsgi import check_password
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.utils.crypto import get_random_string
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

from .models import Company, User, UserOTP, ProfilePicture, CompanyLogo
from .serializers import CompanySerializer, UserSerializer, UserDetailsSerializer, PasswordChangeSerializer
from django.core.exceptions import ValidationError, ObjectDoesNotExist
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
                is_manager=True,
                is_superuser=False,
                is_staff=True
            )
            admin_user.set_password('jikoTrack@2024')
            admin_user.save()

            send_mail(
                'Registration Approved',
                f"""Your registration has been approved. Here are your admin credentials:\n\nUsername: {admin_user.username}\nPassword: jikoTrack@2024.
                    \n We advise you change your password immediately because of security reasons. This password expires after 24 hours""",
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
                    'id': str(company.id),
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

    @action(detail=True, methods=['post'], url_path='upload-logo')
    def upload_logo(self, request, pk=None):
        company = self.get_object()
        file = request.FILES.get('image')
        if not file:
            return Response({"detail": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        company_logo, created = CompanyLogo.objects.get_or_create(company=company)
        company_logo.image = file
        company_logo.save()

        return Response({"detail": "Company logo uploaded successfully"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'], url_path='get-logo')
    def get_logo(self, request, pk=None):
        company = self.get_object()
        if not hasattr(company, 'logo') or not company.logo.image:
            return Response({"detail": "No company logo found"}, status=status.HTTP_404_NOT_FOUND)

        response = HttpResponse(content_type='image/jpeg')
        response['Content-Disposition'] = f'attachment; filename={company.logo.image.name}'
        response.write(company.logo.image.read())
        return response


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

            # Assuming user.company_id is the way to get the company ID associated with the user
            company_id = str(user.company_id)  # Ensure company_id is a string

            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
                'iat': datetime.datetime.utcnow(),
                'sub': str(user.id),
                'company_id': company_id  # Add company_id as a string
            }

            token = jwt.encode(payload, 'secret', algorithm='HS256')

            user_details = {
                'token': token,
                'id': str(user.id),  # Convert UUID to string
                'username': user.username,
                'email': user.email,
                'is_manager': user.is_manager,
                'is_accounting_manager': user.is_accounting_manager,
                'is_inventory_manager': user.is_inventory_manager,
                'is_purchase_manager': user.is_purchase_manager,
                'is_superuser': user.is_superuser
            }

            if not user.is_superuser:
                company = Company.objects.get(id=user.company_id)
                user_details['company_name'] = company.companyName

            response = Response()
            response.set_cookie(key='company_id', value=company_id, httponly=True)  # Set company_id in the cookies
            response.set_cookie(key='jwt', value=token, httponly=True)
            response.data = {
                'jwt': token,
                'user_details': user_details
            }

            return response

        except Company.DoesNotExist:
            return Response({"message": "Company matching query does not exist."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def createUser(self, request):
        try:
            # Role mapping
            role_mapping = {
                'Manager': 'is_manager',
                'Admin': 'is_staff',
                'Accounting Manager': 'is_accounting_manager',
                'Inventory Manager': 'is_inventory_manager',
                'Purchase Manager': 'is_purchase_manager',
                'User': None  # No specific role for 'User'
            }

            # Extract role from request data
            role = request.data.get('role')
            print("Role from request:", role)

            # Add the corresponding role field to request data
            if role:
                role_field = role_mapping.get(role)
                if role_field is not None:
                    request.data[role_field] = True

            print("Request data before serialization:", request.data)

            # Create user using the serializer
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
            else:
                print("Serializer errors:", serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print("Exception occurred:", str(e))
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
                'user_id': str(user.id),
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
                'sub': str(user.id),
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

    @action(detail=False, methods=['post'])
    def newPassword(self, request):
        try:
            new_password = request.data.get('new_password')
            confirm_password = request.data.get('confirm_password')

            if not new_password or not confirm_password:
                raise ValidationError('Both new password and confirm password are required.')

            if new_password != confirm_password:
                raise ValidationError('Passwords do not match.')

            # Locate user by username or email
            username_or_email = request.data.get('username') or request.data.get('email')
            if not username_or_email:
                raise ValidationError('Username or email is required.')

            user = User.objects.filter(Q(username=username_or_email) | Q(email=username_or_email)).first()
            if not user:
                return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

            # Update the user's password
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

            # Check if OTP has expired (OTP is valid for 10 minutes)
            otp_age = timezone.now() - user_otp.created_at
            if otp_age.total_seconds() > 600:  # 600 seconds = 10 minutes
                return Response({'message': 'OTP has expired'}, status=status.HTTP_400_BAD_REQUEST)

            user = user_otp.user
            user.is_active = True
            user.save()

            # Clean up the OTP after successful verification
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

            # Generate random 6-digit OTP
            otp = ''.join(random.choices(string.digits, k=6))

            # Create or update the UserOTP entry
            user_otp, created = UserOTP.objects.get_or_create(user=user)
            user_otp.otp = otp
            user_otp.created_at = timezone.now()  # Ensure the time is timezone-aware
            user_otp.save()

            # Send email with OTP
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

    @action(detail=True, methods=['post'], url_path='upload-profile-picture')
    def upload_profile_picture(self, request, pk=None):
        user = self.get_object()
        file = request.FILES.get('image')
        if not file:
            return Response({"detail": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        profile_picture, created = ProfilePicture.objects.get_or_create(user=user)
        profile_picture.image = file
        profile_picture.save()

        return Response({"detail": "Profile picture uploaded successfully"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'], url_path='get-profile-picture')
    def get_profile_picture(self, request, pk=None):
        user = self.get_object()
        if not hasattr(user, 'profile_picture') or not user.profile_picture.image:
            return Response({"detail": "No profile picture found"}, status=status.HTTP_404_NOT_FOUND)

        response = HttpResponse(content_type='image/jpeg')
        response['Content-Disposition'] = f'attachment; filename={user.profile_picture.image.name}'
        response.write(user.profile_picture.image.read())
        return response

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