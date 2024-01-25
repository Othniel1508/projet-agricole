"""
Django settings for Agricole project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8e&hxd+n7f5lulq54$b)*v&o4h+kto_&avj(bv!h=)3am8(v6u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "Agriculteur.apps.AgriculteurConfig",
    "Consommateur.apps.ConsommateurConfig",
    "Laboratoire.apps.LaboratoireConfig",
    "Transporteur.apps.TransporteurConfig",
    "MarcheAgricole.apps.MarcheagricoleConfig"
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

ROOT_URLCONF = 'Agricole.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Agricole.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'agriculteur': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'agriculteur',
        'USER': 'agriculteur',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306'
    },
    'laboratoire': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'laboratoire',
        'USER': 'laboratoire',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306'
    },
    'marcheagricole': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'marcheagricole',
        'USER': 'marcher',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306'
    },
    'consommateur': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'consommateur',
        'USER': 'consommateur',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306'
    },
    'transporteur': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'transporteur',
        'USER': 'transporteur',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'