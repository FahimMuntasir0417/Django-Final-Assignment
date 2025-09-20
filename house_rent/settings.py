
# import os
# from pathlib import Path
# from datetime import timedelta
# from decouple import config, Csv

# # from rest_framework_nested import routers

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

# # In settings.py
# # SITE_NAME = "Your Site Name"
# # DOMAIN = "yourdomain.com"  # Change this to your actual domain
# # # For development, you can use:
# # # DOMAIN = "localhost:8000"


# # SITE_ID = 1


# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = config("SECRET_KEY")


# # SECURITY WARNING: don't run with debug turned on in production!

# DEBUG = config("DEBUG", default=False, cast=bool)

# # ALLOWED_HOSTS = []

# ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

# # Application definition

# INSTALLED_APPS = [
#     "whitenoise.runserver_nostatic",
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
    
#     'django.contrib.staticfiles',
#     'drf_yasg',

#     'django.contrib.sites',
    
#     # Third party apps
#     'rest_framework',
#     'rest_framework_simplejwt',
#     'djoser',
#     'django_filters',
#     "corsheaders",
#     # 'drf_nested_routers',
    
#     'cloudinary',
#     'cloudinary_storage',
    
#     # Local apps
#     'users',
#     'rent_api',
#     'rent_type',
#     'rent_add',
#     'rent_user',
# ]


# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# # Cloudinary Config
# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME'),
#     'API_KEY': config('CLOUDINARY_API_KEY'),
#     'API_SECRET': config('CLOUDINARY_API_SECRET'),
# }

# # DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# MIDDLEWARE = [
    
    
#     "corsheaders.middleware.CorsMiddleware",

#     'django.middleware.security.SecurityMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'house_rent.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'house_rent.wsgi.app'

# CORS_ALLOWED_ORIGINS = [
#     'http://localhost:5173' ,
#     'https://django-final-assignment.vercel.app'
    
    
    
    
    
    
# ]

# INTERNAL_IPS = [
#     # ...
#     "127.0.0.1",
#     # ...
# ]


# # Database
# # https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# # DATABASES = {
# #     'default': {
# #         'ENGINE': 'django.db.backends.sqlite3',
# #         'NAME': BASE_DIR / 'db.sqlite3',
# #     }
# # }

# # Database
# DATABASES = {
#     'default': {
#         'ENGINE': config("DB_ENGINE"),
#         'NAME': config("DB_NAME"),
#         # Uncomment for PostgreSQL
#          'USER': config("DB_USER"),
#          'PASSWORD': config("DB_PASSWORD"),
#          'HOST': config("DB_HOST"),
#          'PORT': config("DB_PORT"),
#     }
# }






# # Password validation
# # https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# # Internationalization
# # https://docs.djangoproject.com/en/5.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

# USE_I18N = True

# USE_TZ = True


# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/5.2/howto/static-files/

# STATIC_URL = '/static/'
# MEDIA_URL = '/media/'

# STATIC_ROOT = BASE_DIR / "staticfiles"
# # STATIC_FILES_DIR = BASE_DIR / 'static'
# STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

# # MEDIA_ROOT = BASE_DIR / 'media'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# # Default primary key field type
# # https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# # Django REST Framework
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ),
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticated',
#     ],
# }

# # Simple JWT
# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(days=2),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
#     'ROTATE_REFRESH_TOKENS': True,
#     'BLACKLIST_AFTER_ROTATION': True,
#     'AUTH_HEADER_TYPES': ('JWT',),
# }

# # Djoser
# SITE_ID = 1

# DJOSER = {
#     'USER_CREATE_PASSWORD_RETYPE': True,
#     'SEND_ACTIVATION_EMAIL': True,
#     'ACTIVATION_URL': 'activate/{uid}/{token}',
#     'SEND_CONFIRMATION_EMAIL': True,
#     'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
#     'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
#     'SET_USERNAME_RETYPE': True,
#     'SET_PASSWORD_RETYPE': True,
#     'PASSWORD_RESET_CONFIRM_RETYPE': True,
#     'LOGOUT_ON_PASSWORD_CHANGE': True,
    
#     'EMAIL': {
#         'activation': 'djoser.email.ActivationEmail',
#         'confirmation': 'djoser.email.ConfirmationEmail',
#         'password_reset': 'djoser.email.PasswordResetEmail',
#         'password_changed_confirmation': 'djoser.email.PasswordChangedConfirmationEmail',
#     },   
    
#     'SERIALIZERS': {
#         'user_create': 'users.serializers.CustomUserCreateSerializer',
#         'user': 'users.serializers.CustomUserSerializer',
#         'current_user': 'users.serializers.CustomUserSerializer',
#     },
#     'PERMISSIONS': {
#         'user_create': ['rest_framework.permissions.AllowAny'],
#         'user': ['rest_framework.permissions.IsAuthenticated'],
#         'user_list': ['rest_framework.permissions.IsAdminUser'],
#     },
# }


# SWAGGER_SETTINGS = {
#    'SECURITY_DEFINITIONS': {
      
#       'Bearer': {
#             'type': 'apiKey',
#             'name': 'Authorization',
#             'in': 'header'
#       }
#    }
# }





# # Email
# EMAIL_BACKEND = config("EMAIL_BACKEND")
# EMAIL_HOST = config("EMAIL_HOST")
# EMAIL_PORT = config("EMAIL_PORT", cast=int)
# EMAIL_USE_TLS = config("EMAIL_USE_TLS", cast=bool)
# EMAIL_HOST_USER = config("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
# DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL")

# #  zbqr nysx kjgq mhys


# # Custom user model
# AUTH_USER_MODEL = 'users.CustomUser'


# # Login/Logout URLs (optional but recommended)
# LOGIN_URL = '/admin/login/'
# LOGOUT_URL = '/admin/logout/'

import os
from pathlib import Path
from datetime import timedelta
from decouple import config, Csv
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", default=False, cast=bool)
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

# Application definition
INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',
    'django.contrib.sites',
    
    # Third party apps
    'rest_framework',
    'rest_framework_simplejwt',
    'djoser',
    'django_filters',
    "corsheaders",
    
    'cloudinary',
    'cloudinary_storage',
    
    # Local apps
    'users',
    'rent_api',
    'rent_type',
    'rent_add',
    'rent_user',
]

# Cloudinary Configuration - এখানে যোগ করুন
cloudinary.config(
    cloud_name=config('CLOUDINARY_CLOUD_NAME'),
    api_key=config('CLOUDINARY_API_KEY'),
    api_secret=config('CLOUDINARY_API_SECRET'),
    secure=True
)

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': config('CLOUDINARY_API_KEY'),
    'API_SECRET': config('CLOUDINARY_API_SECRET'),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'house_rent.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'house_rent.wsgi.app'

CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    'https://django-final-assignment.vercel.app'
]

INTERNAL_IPS = [
    "127.0.0.1",
]

# Database
DATABASES = {
    'default': {
        'ENGINE': config("DB_ENGINE"),
        'NAME': config("DB_NAME"),
        'USER': config("DB_USER"),
        'PASSWORD': config("DB_PASSWORD"),
        'HOST': config("DB_HOST"),
        'PORT': config("DB_PORT"),
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# Simple JWT
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=2),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('JWT',),
}

# Djoser
SITE_ID = 1

DJOSER = {
    'USER_CREATE_PASSWORD_RETYPE': True,
    'SEND_ACTIVATION_EMAIL': True,
    'ACTIVATION_URL': 'activate/{uid}/{token}',
    'SEND_CONFIRMATION_EMAIL': True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
    'SET_USERNAME_RETYPE': True,
    'SET_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'LOGOUT_ON_PASSWORD_CHANGE': True,
    
    'EMAIL': {
        'activation': 'djoser.email.ActivationEmail',
        'confirmation': 'djoser.email.ConfirmationEmail',
        'password_reset': 'djoser.email.PasswordResetEmail',
        'password_changed_confirmation': 'djoser.email.PasswordChangedConfirmationEmail',
    },   
    
    'SERIALIZERS': {
        'user_create': 'users.serializers.CustomUserCreateSerializer',
        'user': 'users.serializers.CustomUserSerializer',
        'current_user': 'users.serializers.CustomUserSerializer',
    },
    'PERMISSIONS': {
        'user_create': ['rest_framework.permissions.AllowAny'],
        'user': ['rest_framework.permissions.IsAuthenticated'],
        'user_list': ['rest_framework.permissions.IsAdminUser'],
    },
}

SWAGGER_SETTINGS = {
   'SECURITY_DEFINITIONS': {
      'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
      }
   }
}

# Email
EMAIL_BACKEND = config("EMAIL_BACKEND")
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_PORT = config("EMAIL_PORT", cast=int)
EMAIL_USE_TLS = config("EMAIL_USE_TLS", cast=bool)
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL")

# Custom user model
AUTH_USER_MODEL = 'users.CustomUser'

# Login/Logout URLs
LOGIN_URL = '/admin/login/'
LOGOUT_URL = '/admin/logout/'