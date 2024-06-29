import random
import string
import uuid

from PIL import Image
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone


class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    country_code = models.CharField(max_length=10, blank=True, null=True)
    number = models.CharField(max_length=255)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=255)
    zone = models.CharField(max_length=255)
    companyName = models.CharField(max_length=255, default='None')
    language = models.CharField(max_length=255, default='None')
    companySize = models.CharField(max_length=255, default='None')
    primaryInterest = models.CharField(max_length=255, default='None')
    is_approved = models.BooleanField(default=False)
    password = models.CharField(max_length=128, default=False)

    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company')

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_manager', True)

        return self.create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    is_manager = models.BooleanField(default=False)
    is_accounting_manager = models.BooleanField(default=False)
    is_inventory_manager = models.BooleanField(default=False)
    is_purchase_manager = models.BooleanField(default=False)
    address1 = models.CharField(max_length=255, null=True, blank=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    email2 = models.EmailField(null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.CharField(max_length=20, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)

    objects = UserManager()

    def __str__(self):
        return self.username


class UserOTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=8, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_otp(self):
        self.otp = ''.join(random.choices(string.digits, k=8))
        self.created_at = timezone.now()  # Ensure the time is timezone-aware
        self.save()


class ProfilePicture(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='profile_picture')
    image = models.ImageField(upload_to='profile_pictures/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.compress_image()

    def compress_image(self):
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class CompanyLogo(models.Model):
    company = models.OneToOneField('Company', on_delete=models.CASCADE, related_name='logo')
    image = models.ImageField(upload_to='company_logos/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.compress_image()

    def compress_image(self):
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
