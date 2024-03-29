"""
Django settings for TimeZone project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""


import os
import django_on_heroku
from pathlib import Path

#to safe secret key


SECRET_KEY = str(os.getenv('SECRET_KEY'))
RAZOR_KEY_SECRET = '7hOFVJSDn4Po1wyGPARzH9o6'
RAZOR_KEY_ID='rzp_test_8cWmlnkYHYznrK'


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# <- New




# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'category',
    'store',
    'accounts',
    'adminpanel',
    'cart',
    'orders',
    'mathfilters',
    'django_filters',
    'crispy_forms',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TimeZone.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.counter',
            ],
        },
    },
]

WSGI_APPLICATION = 'TimeZone.wsgi.application'

AUTH_USER_MODEL = 'accounts.Account'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'timezone',
#         'USER': 'postgres',
#         'PASSWORD': '123456789',
#         'HOST': 'timezone.ctlcsro6cbs6.ap-south-1.rds.amazonaws.com',
#         'PORT': '5432',

#     }
# }
# local database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd42e7a1f9d5fu8',
        'USER': 'wkwrijybhdzkdj',
        'PASSWORD': 'ebd5693e0b067a7d7a449c9b202080a32a1ee8ce3fd46cdb1adea2bc3183e90b',
        'HOST': 'ec2-44-206-137-96.compute-1.amazonaws.com',
        'PORT': '5432',

    }
}

# DATABASES = {
#     'default' :{
#         'ENGINE' : 'django.db.backends.sqlite3',
#         'NAME' : BASE_DIR/ 'db.sqlite3'
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE =  'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# STATIC_URL = '/static/'

# STATICFILES_DIRS = [ 
#     os.path.join('static')
# ]

# # when doing collectstatic all static files will take from STATICFILES_DIRS and put in in STATC_ROOT
# # on deploy we will create 'django.conf' file on sites-availbale and will tell that toot  
# STATIC_ROOT ='statics'

# #media files
# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR/'media'


# for herukuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu

django_on_heroku.settings(locals())
STATIC_ROOT = 'staticfiles'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    (os.path.join(BASE_DIR,'smcore','static')),
)


STATICFILES_FINDERS = (

    #'django.contrib.staticfiles.finders.FileSystemFinder',
    #'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# end heroku



# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#to secure cookie in razor payment
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
# CSRF_COOKIE_SAMESITE = 'None'
# SESSION_COOKIE_SAMESITE = 'None'


# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True

CRISPY_TEMPLATE_PACK = 'bootstrap4'