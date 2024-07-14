from django.contrib import admin
from django.core.mail import send_mail

from .models import Company, User, UserOTP

admin.site.register(Company)
admin.site.register(User)
admin.site.register(UserOTP)
