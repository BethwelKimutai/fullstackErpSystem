from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Company, User, ProfilePicture


class CompanySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex', read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'email', 'is_approved', 'password', 'address', 'country', 'number', 'city', 'zone',
                  'language', 'primaryInterest', 'companySize', 'companyName']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex', read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_manager', 'company', 'is_accounting_manager',
                  'is_inventory_manager', 'is_purchase_manager', 'is_active', 'date_joined', 'first_name', 'last_name',
                  'address1', 'address2', 'email2', 'country', 'state', 'zip_code', 'profile_picture']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)

        role = validated_data.get('role', None)
        if role:
            instance.is_manager = (role == 'Manager')
            instance.is_accounting_manager = (role == 'Accounting Manager')
            instance.is_inventory_manager = (role == 'Inventory Manager')
            instance.is_purchase_manager = (role == 'Purchase Manager')

        instance.save()
        return instance


class PasswordResetSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def save(self, user):
        user.password = make_password(self.validated_data['new_password'])
        user.save()
        return user


class UserDetailsSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    is_manager = serializers.BooleanField(default=False)
    is_accounting_manager = serializers.BooleanField(default=False)
    is_inventory_manager = serializers.BooleanField(default=False)
    is_purchase_manager = serializers.BooleanField(default=False)
    company_name = serializers.SerializerMethodField()

    def get_company_name(self, obj):
        return obj.company.companyName if obj.company else None


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("New passwords do not match")
        return data


class ProfilePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilePicture
        fields = ['image']
