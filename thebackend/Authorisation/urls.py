from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from .views import CompanyViewSet, UserViewSet

urlpatterns = [
    path('users/login/', UserViewSet.as_view({'post': 'login'}), name='user-login'),
    path('users/profilepic/set/', UserViewSet.as_view({'post': 'upload_profile_picture'}), name='user-profile-pic'),
    path('users/adduserinfo/', UserViewSet.as_view({'post': 'update_user_info'}), name='user-adduser-info'),
    path('users/getallusers/', UserViewSet.as_view({'get': 'getAllUsers'}), name='user-get-all-users'),
    path('users/logout/', UserViewSet.as_view({'post': 'logout'}), name='user-logout'),
    path('users/getuser/', UserViewSet.as_view({'post': 'getUsers'}), name='user-get-user'),
    path('users/createuser/', UserViewSet.as_view({'post': 'createUser'}), name='user-create'),
    path('users/newpassword/', UserViewSet.as_view({'post': 'newPassword'}), name='user-new-password'),
    path('users/forgotpassword/', UserViewSet.as_view({'post': 'forgotPassword'}), name='user-forgot-password'),
    path('users/forgotpasswordotpverification/', UserViewSet.as_view({'post': 'forgotPasswordOtpVerification'}),
         name='user-forgot-password-verification'),
    path('companies/register/', CompanyViewSet.as_view({'post': 'register'}), name='company-register'),
    path('companies/<uuid:pk>/approve/', CompanyViewSet.as_view({'post': 'approve'}), name='company-approve'),
    path('users/updateuser/<uuid:pk>/', UserViewSet.as_view({'put': 'updateUser'}), name='update-user'),
    path('users/deleteuser/<uuid:pk>/', UserViewSet.as_view({'delete': 'delete'}), name='delete-user'),
    path('users/getuserbyid/<uuid:pk>/', UserViewSet.as_view({'get': 'getUserById'}), name='get-user-bi-id'),
    path('users/roles/', UserViewSet.as_view({'get': 'roles'}), name='get-roles'),
    path('users/authcheck/', UserViewSet.as_view({'get': 'authChecker'}), name='check-auth'),
    path('companies/getcompanies/', CompanyViewSet.as_view({'get': 'companiesList'}), name='get-companies'),
    path('companies/getallcompanies/', CompanyViewSet.as_view({'get': 'getAllCompanies'}), name='get-all-companies'),
    path('users/signout/', UserViewSet.as_view({'post': 'sign_out'}), name='user-signout'),
    path('users/signin/', UserViewSet.as_view({'post': 'sign_in'}), name='user-signin'),
    path('users/avatar/', UserViewSet.as_view({'post': 'upload_user_avatar'}), name='user-avatar'),
    path('companies/logo/', CompanyViewSet.as_view({'post': 'upload_company_logo'}), name='company-logo'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
