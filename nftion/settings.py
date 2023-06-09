"""
Django settings for nftion project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
# import cloudinary
# import cloudinary.uploader
# import cloudinary.api
import cloudinary
import cloudinary.uploader
import cloudinary.api
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from celery.schedules import crontab
from urllib3.exceptions import InsecureRequestWarning

import warnings
BASE_DIR = Path(__file__).resolve().parent.parent

cloudinary.config( 
  cloud_name = "duj1bqena", 
  api_key = "532781915438853", 
  api_secret = "nAxLJl_tX62II-smUVAltdoOEc0" 
)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd#cyiwv#!=ophz+_&#%^#d4w)or8#gn#!6$rqzh^os851)nka&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['nftion.io', '127.0.0.1', 'nftion-nft-website-test.herokuapp.com']

CSRF_TRUSTED_ORIGINS = ['https://nftion.io', 'http://127.0.0.1:8000/', 'http://nftion-nft-website-test.herokuapp.com/']


warnings.filterwarnings("ignore", category=InsecureRequestWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django_celery_beat',
    'home',
    'auth_app',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.twitter',
    'cloudinary',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SITE_ID = 3

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email', 'openid'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'VERIFIED_EMAIL': True,
    },
    'facebook': {
        'METHOD': 'oauth2',
        'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
        'SCOPE': ['email', 'public_profile'],

        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'first_name',
            'last_name',
            'middle_name',
            'name',
            'name_format',
            'picture',
            'short_name'
        ],
        'VERIFIED_EMAIL': True,
    },
    'linkedin_oauth2': {
        'SCOPE': [
            # 'r_basicprofile',
            'r_liteprofile',
            'r_emailaddress',
            # 'r_fullprofile',
            # 'w_member_social',
        ],
        'PROFILE_FIELDS': [
            'id',
            'first-name',
            'last-name',
            'email-address',
            'picture-url',
            'public-profile-url',
        ],
        'VERIFIED_EMAIL': True,
    },
    'twitter': {
        'SCOPE': ['email'],
        'VERIFIED_EMAIL': True,
    }
}
AUTHENTICATION_BACKENDS = (
    'auth_app.backends.EmailBackend',
    'allauth.account.auth_backends.AuthenticationBackend',

)
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_FORMS = {
    'login': 'allauth.account.forms.LoginForm',
    # 'login': 'users.forms.MyCustomLoginForm',
    # 'signup': 'allauth.account.forms.SignupForm',
    'signup': 'auth_app.forms.SimpleSignupForm',
    'add_email': 'allauth.account.forms.AddEmailForm',
    'change_password': 'allauth.account.forms.ChangePasswordForm',
    'set_password': 'allauth.account.forms.SetPasswordForm',
    'reset_password': 'allauth.account.forms.ResetPasswordForm',
    'reset_password_from_key': 'allauth.account.forms.ResetPasswordKeyForm',
    'disconnect': 'allauth.socialaccount.forms.DisconnectForm',
}


ROOT_URLCONF = 'nftion.urls'

DEFAULT_HOST = ' '

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'home.context_processor.get_user_profile_e'
            ],
        },
    },
]
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

WSGI_APPLICATION = 'nftion.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
AUTH_USER_MODEL = 'auth_app.MyUser'

API_KEY = '951c3c7aede140f0ac60d27aa9e35208'
API_KEY_HISTORICAL = 'e88255fe31204562dfccf2027f6ca3' \
                     '' \
                     '0353abb2d3c460bdae025014ff421adb00'

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
# ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_UNIQUE_USERNAME = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True
# SOCIALACCOUNT_ADAPTER = 'home.adapters.CustomSocialAccountAdapter'
SOCIALACCOUNT_LOGIN_ON_GET=True

ACCOUNT_SIGNUP_REDIRECT_URL = 'home:dashboard'
LOGIN_URL = 'account_login'
LOGIN_REDIRECT_URL = 'home:dashboard'
LOGOUT_REDIRECT_URL = 'home:home'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'support@nftion.io'
EMAIL_HOST_PASSWORD = 'elfumuwudqmvwsys'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

CELERY_BROKER_URL = os.getenv('REDIS_URL')
CELERY_RESULT_BACKEND = os.getenv('REDIS_URL')
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
CELERY_TIMEZONE = "UTC"


# REDIS_URL = "redis://:p28fd02cacae7f0c7e54e799f3f6745fbeb7258cd54c349e2bc16d59ff512fc0a@ec2-34-250-52-181.eu-west-1.compute.amazonaws.com:19339"
# # First, parse the Redis URL
# redis_url = REDIS_URL
# redis_parsed = redis_urlparse.urlparse(redis_url)

# # Define the Django Redis settings
# REDIS_HOST = redis_parsed.hostname
# REDIS_PORT = redis_parsed.port
# REDIS_PASSWORD = redis_parsed.password
# REDIS_DB = 0

# # Use the Django Redis cache backend
# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': f'redis://{REDIS_HOST}:{REDIS_PORT}/1',
#         'OPTIONS': {
#             'PASSWORD': REDIS_PASSWORD,
#             'DB': REDIS_DB,
#         },
#         'TIMEOUT': None,
#     }
# }

# # Use the Django Redis Celery broker
# BROKER_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/0'
# BROKER_TRANSPORT_OPTIONS = {
#     'password': REDIS_PASSWORD,
#     'db': REDIS_DB,
# }

# # Use the Django Redis Celery result backend
# CELERY_RESULT_BACKEND = f'redis://{REDIS_HOST}:{REDIS_PORT}/0'
# CELERY_RESULT_BACKEND_TRANSPORT_OPTIONS = {
#     'password': REDIS_PASSWORD,
#     'db': REDIS_DB,
# }


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

FAIL_SILENTLY_EMAIL = False

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATIC_URL = '/static/'
# # STATICFILES_LOCATION = 'static'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, "static/media_root")
prod_db = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)


STATIC_URL = 'static/'
MEDIA_URL = '/media_root/'
STATICFILES_LOCATION = 'staticfiles'
MEDIA_ROOT = os.path.join(BASE_DIR, "static/media_root")

PROJECT_ROOT = os.path.join(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
