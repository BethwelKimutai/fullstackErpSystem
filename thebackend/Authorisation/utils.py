# utils.py

import jwt
from datetime import datetime, timedelta
from django.conf import settings

from Authorisation.models import User


def generate_jwt(user):
    payload = {
        'user_id': str(user.id),
        'username': user.username,
        'email': user.email,
        'is_manager': user.is_manager,
        'is_accounting_manager': user.is_accounting_manager,
        'is_inventory_manager': user.is_inventory_manager,
        'is_purchase_manager': user.is_purchase_manager,
        'is_superuser': user.is_superuser,
        'exp': datetime.utcnow() + timedelta(days=1),  # Token expiration time
        'iat': datetime.utcnow()  # Token issue time
    }

    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

    return token

# Function to decode JWT token
def decode_jwt(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        user_id = payload.get('user_id')
        user = User.objects.get(id=user_id)

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

        return user_details
    except jwt.ExpiredSignatureError:
        return None  # Token is expired
    except jwt.InvalidTokenError:
        return None  # Invalid token
    except User.DoesNotExist:
        return None  # User does not exist