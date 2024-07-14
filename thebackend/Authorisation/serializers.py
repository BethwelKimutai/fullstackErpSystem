from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Company, User, ProfilePicture


class CompanySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex', read_only=True)
<<<<<<< HEAD

    class Meta:
        model = Company
        fields = [
            'id', 'name', 'email', 'is_approved', 'address', 'country', 'number', 'city', 'zone',
            'language', 'primaryInterest', 'companySize', 'companyName'
        ]
=======
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'email', 'is_approved', 'password', 'address', 'country', 'number', 'city', 'zone',
                  'language', 'primaryInterest', 'companySize', 'companyName']
>>>>>>> e5ef20e6faa5594b57c646fde9c033923d255356

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = super().create(validated_data)
        if password:
            instance.set_password(password)
            instance.save()
        return instance

    def createLogo(self, validated_data):
        logo = validated_data.pop('logo', None)
        instance = super().create(validated_data)
        if logo:
            instance.logo = logo
            instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex', read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
<<<<<<< HEAD
        fields = [
            'id', 'username', 'email', 'password', 'is_manager', 'company', 'is_accounting_manager',
            'is_inventory_manager', 'is_purchase_manager', 'is_active', 'date_joined', 'first_name', 'last_name',
            'address1', 'address2', 'email2', 'country', 'state', 'zip_code', 'avatar'
        ]
=======
        fields = ['id', 'username', 'email', 'password', 'is_manager', 'company', 'is_accounting_manager',
                  'is_inventory_manager', 'is_purchase_manager', 'is_active', 'date_joined', 'first_name', 'last_name',
                  'address1', 'address2', 'email2', 'country', 'state', 'zip_code', 'profile_picture']
>>>>>>> e5ef20e6faa5594b57c646fde9c033923d255356

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


<<<<<<< HEAD
class CompanyLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['logo']

    def update(self, instance, validated_data):
        instance.logo = validated_data.get('logo', instance.logo)
        instance.save()
        instance.compress_image()
        return instance


class UserAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['avatar']

    def update(self, instance, validated_data):
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.save()
        instance.compress_image()
        return instance

class UserLoginSerializer(serializers.Serializer):
    access = serializers.CharField()
    user_details = serializers.DictField()
=======
class ProfilePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilePicture
        fields = ['image']
>>>>>>> e5ef20e6faa5594b57c646fde9c033923d255356
