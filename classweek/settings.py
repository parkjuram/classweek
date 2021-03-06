"""
Django settings for classweek project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import warnings
warnings.filterwarnings(
        'error', r"DateTimeField .* received a naive datetime",
        RuntimeWarning, r'django\.db\.models\.fields')

from datetime import datetime
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

CHARSET = 'utf-8'

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

from os.path import join, abspath, dirname
here = lambda *dirs: join(abspath(dirname(__file__)), *dirs)
T_BASE_DIR = here('..')
root = lambda *dirs: join(abspath(T_BASE_DIR), *dirs)

TEMPLATE_DIRS = (
    root('templates'),
)

ALLOWED_HOSTS = ['*']

# TEMPLATE_DIRS = (
#     PROJECT_PATH + '/templatesss/'
# )


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&e3==uq7$-p(k_&bxj(@h5q*3oe-@g+xnggz%o3#9y3+z@fx%v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

# Needed when DEBUG=False
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'user',
    'classes',
    'forcompany',
    'forcompany.templatetags',
    'foradmin',
    'analysis',
    'csvimport',
    'bootstrap3',
    'registration',
)

SITE_ID = 1

ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'custom_middleware.logger.ApiCallLogger',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
)

SWAGGER_SETTINGS = {
    "exclude_namespaces": [], # List URL namespaces to ignore
    "api_version": '0.1',  # Specify your API's version
    "api_path": "/",  # Specify the path to your API not a root level
    "enabled_methods": [  # Specify which methods to enable in Swagger UI
        'get',
        'post',
        'put',
        'patch',
        'delete'
    ],
    "api_key": '', # An API key
    "is_authenticated": False,  # Set to True to enforce user authentication,
    "is_superuser": False,  # Set to True to enforce admin only access
}

ROOT_URLCONF = 'classweek.urls'

WSGI_APPLICATION = 'classweek.wsgi.application'


# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file_all': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': datetime.now().strftime('log/all_%d_%m_%Y.log'),
            'formatter': 'verbose'
        },
        'file_foradmin': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': datetime.now().strftime('log/foradmin_%d_%m_%Y.log'),
            'formatter': 'verbose'
        },
        'file_payment': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': datetime.now().strftime('log/payment_%d_%m_%Y.log'),
            'formatter': 'verbose'
        },
        'file_classes':{
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': datetime.now().strftime('log/classes_%d_%m_%Y.log'),
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'foradmin': {
            'handlers': ['file_all', 'file_foradmin'],
            'level': 'DEBUG',
        },
        'classes': {
            'handlers': ['file_all', 'file_classes'],
            'level': 'DEBUG',
        },
        'payment': {
            'handlers': ['file_all', 'file_payment'],
            'level': 'DEBUG',
        },
    }
}


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'classweek',
        'USER': 'blackpigstudio',
        'PASSWORD': 'bestStartup2014!',
        'HOST': 'localhost',
        'PORT': '',
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, '../database/db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_TZ = True
TIME_ZONE = 'Asia/Seoul'

# USE_I18N = True
#
# USE_L10N = True




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../static')

# AUTH_PROFILE_MODULE = 'user.UserProfile'

# @login_request
LOGIN_URL = '/user/login'

SOUTH_TESTS_MIGRATE = False # To disable migrations and use syncdb instead
SKIP_SOUTH_TESTS = True # To disable South's own unit tests

EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'parkjuram@gmail.com'
EMAIL_HOST_PASSWORD = '5OxPtrdEVEer03KbvS1wRQ'
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'classweek2014@gmail.com'
# EMAIL_USE_TLS = True