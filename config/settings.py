from pathlib import Path

import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(BASE_DIR / ".env")


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = env("ALLOWED_HOSTS", default="").split(",")

DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

SERVICE_APPS = [
    "rest_framework",
    "django_filters",
    "drf_yasg",
    'corsheaders',  # для headers - см.ниже переменную CORS_ALLOWED_ORIGINS + Middleware
    'rest_framework.authtoken',
]

APPS = [
    "apps.core.apps.CoreConfig",
    "apps.orders.apps.OrdersConfig",
]

INSTALLED_APPS = DEFAULT_APPS + SERVICE_APPS + APPS

CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOWED_ORIGINS = [
#     "https://localhost:8080",
#     "https://127.0.0.1:8080",
# ]


MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # он должен стоять выше всех, так сказано
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": env("DB_ENGINE", default="django.db.backends.postgresql"),
        "NAME": env("POSTGRES_DB", default=""),
        "USER": env("POSTGRES_USER", default=""),
        "PASSWORD": env("POSTGRES_PASSWORD", default=""),
        "HOST": env("POSTGRES_HOST", default="localhost"),
        "PORT": env("POSTGRES_PORT", cast=int, default=5432),
        "ATOMIC_REQUESTS": True,
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
#     },
# ]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/


LANGUAGE_CODE = "en-US"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# if DEBUG:
#     LOGGING = {
#         "version": 1,
#         "filters": {
#             "require_debug_true": {
#                 "()": "django.utils.log.RequireDebugTrue",
#             }
#         },
#         "handlers": {
#             "console": {
#                 "level": "DEBUG",
#                 "filters": ["require_debug_true"],
#                 "class": "logging.StreamHandler",
#             }
#         },
#         "loggers": {
#             "django.db.backends": {
#                 "level": "DEBUG",
#                 "handlers": ["console"],
#             }
#         },
#     }

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',  # вот здесь импорт делать из рест-фреймворк, а не из джанго-филтер
        'rest_framework.filters.OrderingFilter',  # и здесь тоже
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated',
    #     'rest_framework.permissions.IsAdminUser',
    # ],
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 20,  # количество элементов на одной странице для пагинации
}

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SWAGGER_SETTINGS = {
    'LOGIN_URL': '/admin/login/',
    'LOGOUT_URL': '/admin/logout/',
    'DEFAULT_INFO': 'config.api_docs.openapi_info',
}

ORDERS_PER_PAGE = 3
