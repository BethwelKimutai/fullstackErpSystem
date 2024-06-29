# views.py
from django.shortcuts import render, redirect
from .forms import CompanyForm, UserLoginForm, ForgotPasswordForm, ResetPasswordForm, UserProfileForm, \
    CompanyProfileForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


def signup_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = CompanyForm()
    return render(request, 'signup_company.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def forgot_password(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            # Handle OTP generation and send
            pass
    else:
        form = ForgotPasswordForm()
    return render(request, 'forgot_password_step1.html', {'form': form})


def reset_password(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            # Handle password reset
            pass
    else:
        form = ResetPasswordForm()
    return render(request, 'forgot_password_step2.html', {'form': form})


def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'user_profile.html', {'form': form})


def company_profile(request):
    if request.method == 'POST':
        form = CompanyProfileForm(request.POST, request.FILES, instance=request.user.company)
        if form.is_valid():
            form.save()
    else:
        form = CompanyProfileForm(instance=request.user.company)
    return render(request, 'company_profile.html', {'form': form})


