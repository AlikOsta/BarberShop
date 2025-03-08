
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = True if os.getenv('DEBUG', 'True') == 'True' else False

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'jazzmin', 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'captcha',
    'app',
    
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

ROOT_URLCONF = 'barber.urls'

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

WSGI_APPLICATION = 'barber.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = os.getenv('LANGUAGE_CODE')

TIME_ZONE = os.getenv('TIME_ZONE')

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static', 
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

YOUR_PERSONAL_CHAT_ID = os.getenv("YOUR_PERSONAL_CHAT_ID")

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY") 

JAZZMIN_SETTINGS = {
    "site_title": "Barbershop Admin",
    "site_header": "Barbershop",
    "site_brand": "Под Горшок",
    "site_logo": "images/logo.png",
    "welcome_sign": "Добро пожаловать в Barbershop 'Под Горшок'",

    "icons": {
        "app.Visit": "fas fa-calendar-check",
        "app.Master": "fas fa-user-tie",
        "app.Service": "fas fa-cut",
        "app.Review": "fas fa-star",
        "auth.User": "fas fa-users-cog",
        "auth.Group": "fas fa-users",
    },
    
}

CAPTCHA_FONT_SIZE = 30
CAPTCHA_LENGTH = 6
CAPTCHA_BACKGROUND_COLOR = '#ffffff'
CAPTCHA_FOREGROUND_COLOR = '#000000'
CAPTCHA_NOISE_FUNCTIONS = ('captcha.helpers.noise_dots',)


