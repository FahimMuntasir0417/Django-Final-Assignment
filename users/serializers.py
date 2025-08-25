from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers
from django.core.validators import RegexValidator
from .models import CustomUser

class CustomUserCreateSerializer(BaseUserCreateSerializer):
    phone_number = serializers.CharField(
        max_length=15,
        required=False,
        allow_blank=True,
        allow_null=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )

    class Meta(BaseUserCreateSerializer.Meta):
        model = CustomUser
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 
                 'phone_number', 'profile_image', 'role')

class CustomUserSerializer(BaseUserSerializer):
    profile_image_url = serializers.SerializerMethodField()

    class Meta(BaseUserSerializer.Meta):
        model = CustomUser
        fields = (
            'id', 'email', 'first_name', 'last_name', 'phone_number',
            'profile_image', 'profile_image_url', 'role', 
            'is_verified', 'is_active', 'created_at', 'last_login'
        )
        read_only_fields = ('id', 'email', 'is_verified', 'created_at', 'last_login')

    def get_profile_image_url(self, obj):
        request = self.context.get('request')
        if obj.profile_image and hasattr(obj.profile_image, 'url'):
            if request:
                return request.build_absolute_uri(obj.profile_image.url)
            return obj.profile_image.url
        return None

class UserProfileUpdateSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(
        max_length=15,
        required=False,
        allow_blank=True,
        allow_null=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )

    class Meta:
        model = CustomUser
        fields = ( 'id', 'first_name', 'last_name', 'phone_number', 'profile_image')
        extra_kwargs = {
            'profile_image': {'required': False}
        }

class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('profile_image',)