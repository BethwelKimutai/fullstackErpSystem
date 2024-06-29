# forms.py
from django import forms
from .models import Company, User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'email', 'country', 'phone', 'address', 'city', 'zone', 'companyName', 'language',
                  'companySize', 'primaryInterest', 'website', 'logo']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label=("Password"), strip=False,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class ForgotPasswordForm(forms.Form):
    username = forms.CharField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))


class ResetPasswordForm(forms.Form):
    otp = forms.CharField(max_length=8, required=True, widget=forms.TextInput(attrs={'placeholder': 'OTP'}))
    new_password = forms.CharField(max_length=254, required=True,
                                   widget=forms.PasswordInput(attrs={'placeholder': 'New Password'}))
    confirm_password = forms.CharField(max_length=254, required=True,
                                       widget=forms.PasswordInput(attrs={'placeholder': 'Confirm New Password'}))


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'address1', 'address2', 'country', 'state', 'zip_code', 'avatar']


class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'email', 'country', 'phone', 'address', 'city', 'zone', 'companyName', 'language',
                  'companySize', 'primaryInterest', 'website', 'logo']
