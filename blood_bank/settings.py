from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
import environ
env = environ.Env()
environ.Env.read_env()
import dj_database_url
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")
CSRF_TRUSTED_ORIGINS = ['https://bindu-blood-bank.onrender.com', 'https://*.127.0.0.1']
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'cloudinary_storage',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # cloudinary
    'django.contrib.staticfiles',
    # Tailwind
    'tailwind',
    'theme',
    'django_browser_reload',
    #apps
    'core',
    'account',
    'history',
    'event',

    'cloudinary',
]

TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1", '*'
]

NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"

MIDDLEWARE = [
    
    'django.middleware.security.SecurityMiddleware',
    # "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = 'blood_bank.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'blood_bank.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

#OnRender Postgre database connection
DATABASES = {
    'default': dj_database_url.config(
        # Feel free to alter this value to suit your needs.
        default=env("DATABASE_LINK"),
    )
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
STATICFILES_DIRS = [BASE_DIR/ 'static']
STATICFILES_ROOT = BASE_DIR/ 'static'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'

MEDIA_URL = 'media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Email Setting
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")

# Setup Cloudnary cloud as file storage
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env("CLOUDINARY_CLOUD_NAME"),
    'API_KEY': env("CLOUDINARY_API_KEY"),
    'API_SECRET': env("CLOUDINARY_API_SECRET"),
    # 'STATICFILES_MANIFEST_ROOT': os.path.join(BASE_DIR, 'my-manifest-directory')
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'