from django.urls import path
from .views import CompanyViewSet, UserViewSet

urlpatterns = [
    path('users/login/', UserViewSet.as_view({'post': 'login'}), name='user-login'),
    path('users/getallusers/', UserViewSet.as_view({'get': 'getAllUsers'}), name='user-get-all-users'),
    path('users/logout/', UserViewSet.as_view({'post': 'logout'}), name='user-logout'),
    path('users/getuser/', UserViewSet.as_view({'get': 'getUsers'}), name='user-get-user'),
    path('users/createuser/', UserViewSet.as_view({'post': 'createUser'}), name='user-create'),
    path('users/newpassword/', UserViewSet.as_view({'post': 'newPassword'}), name='user-new-password'),
    path('users/forgotpassword/', UserViewSet.as_view({'post': 'forgotPassword'}), name='user-forgot-password'),
    path('users/forgotpasswordotpverification/', UserViewSet.as_view({'post': 'forgotPasswordOtpVerification'}),
         name='user-forgot-password-verification'),
    path('companies/register/', CompanyViewSet.as_view({'post': 'register'}), name='company-register'),
    path('companies/<int:pk>/approve/', CompanyViewSet.as_view({'post': 'approve'}), name='company-approve'),
    path('users/updateuser/<int:user_id>/', UserViewSet.as_view({'put': 'updateUser'}), name='update-user'),
    path('users/deleteuser/<int:user_id>/', UserViewSet.as_view({'delete': 'delete'}), name='delete-user'),
    path('users/getuserbyid/<int:user_id>/', UserViewSet.as_view({'get': 'getUserById'}), name='get-user-bi-id'),
    path('users/roles/', UserViewSet.as_view({'get': 'roles'}), name='get-roles'),
    path('users/authcheck/', UserViewSet.as_view({'get': 'authChecker'}), name='check-auth'),
    path('companies/getcompanies/', CompanyViewSet.as_view({'get': 'companiesList'}), name='get-companies'),
    path('companies/getallcompanies/', CompanyViewSet.as_view({'get': 'getAllCompanies'}), name='get-all-companies'),
    path('users/signout/', UserViewSet.as_view({'post': 'sign_out'}), name='user-signout'),
    path('users/signin/', UserViewSet.as_view({'post': 'sign_in'}), name='user-signin'),

]
