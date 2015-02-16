"""
Django settings for website project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&00qubg6jjbl_f8nh%r3ex$@(h_5uhk4j7$shs&__jc66sn#_u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    #---
    'crispy_forms',
    #'allauth',
    #'allauth.account',
    #'allauth.socialaccount',
    #'allauth.socialaccount.providers.facebook',
    'general',
    'orfik',
    'logo',
    'bootstrapform',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'website.urls'

WSGI_APPLICATION = 'website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = None

USE_I18N = False

USE_L10N =False

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL='/media/'
STATIC_ROOT=os.path.join(BASE_DIR,'static_files')
MEDIA_ROOT=os.path.join(BASE_DIR,'media_files')
#-----------
TEMPLATE_DIRS=[os.path.join(BASE_DIR,'templates')]
STATICFILES_DIRS=[os.path.join(BASE_DIR,'staticfiles')]
#-----------
LOGIN_REDIRECT_URL='/'
LOGIN_URL='/'
SITE_ID=1
#------------------
#AUTHENTICATION_BACKENDS = (
#    # Needed to login by username in Django admin, regardless of `allauth`
#    "django.contrib.auth.backends.ModelBackend",
#    # `allauth` specific authentication methods, such as login by e-mail
#    #"allauth.account.auth_backends.AuthenticationBackend",
#)
##TEMPLATE_CONTEXT_PROCESSORS = (
#    #'django.contrib.auth.context_processors.auth',
#    # Required by allauth template tags
#    #"django.core.context_processors.request",
#    # allauth specific context processors
#    #"allauth.account.context_processors.account",
#    #"allauth.socialaccount.context_processors.socialaccount",
#)
#---------------------Allauth settings

ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_USERNAME_REQUIRED =True

#ACCOUNT_EMAIL_REQUIRED=True
#ACCOUNT_USERNAME_REQUIRED =True
