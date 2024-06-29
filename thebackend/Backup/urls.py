from django.urls import path
from . import views

urlpatterns = [
    # Company related URLs
    path('signup/company/', views.signup, name='company-signup'),
    path('company/login/', views.login, name='company-login'),
    path('company/forgot_password/', views.forgot_password, name='company-forgot-password'),
    path('company/profile/<uuid:pk>/', views.company_profile, name='company-profile'),

    # User related URLs
    path('signup/user/', views.signup, name='user-signup'),
    path('login/', views.login, name='user-login'),
    path('forgot_password/', views.forgot_password, name='user-forgot-password'),
    path('profile/<uuid:pk>/', views.user_profile, name='user-profile'),
]