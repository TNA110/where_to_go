from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent
SECRET_KEY = "E}KptzM41Lpz~cw3TF#NYW5J|lNj4m3Pt2~U0J{d4ne71Z2OyZKMGUdCr%oIouAZ0Z$LuCclhd*FGUwLxaFYJQ2PeGoHm}6VcgivlN95o1azAyXna}H*}Wm6jc#*LpkEkXyC4yEMEntLKk#$~THyoaB0Xz%ah1daLs9@M5nIXZg**tFIM#xyIKtRTm~v0bUPqp}eRY7qv#%HxHt%0sXlychLA7hlXX$gl0}cyu?9tME~TEknp?PQ$e97h4A9iPlBZ?VCivNyTpycvEBdA}IC6vlZNerAi{D~bpzC6PBg~A8Qq$4twi8h?l?b829a%JC5{vJVr6|0PEirnLZtwc2|Ym*{qiaOmoL~h7}ZPER2$@1uBxG?m}WQSMxFJ4ZzhV3~jgazR{65?hFZonL~Wt0Wq3oYbCp8}LQ*e6glUiAxTG2J2P?z5aPcW~hR~DS~xNlN{IctWW#EB~BmK1Wqep9%6@YX@@WW}?9B?F0{*}Mv}XJJVBV|DZv"
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
SECURE_HSTS_PRELOAD = False
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', ".pythonanywhere.com"]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'where_to_go',
    'adminsortable2',
    'tinymce',
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

ROOT_URLCONF = 'where_to_go.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'where_to_go.wsgi.application'

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

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'assets'),)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
