import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("DJANGO_SECRET", "dev-secret-key")
DEBUG = True
ALLOWED_HOSTS = ["*"]

# -------------------------------------------------------
# Installed apps
# -------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "channels",      # WebSockets
    "chatapp",       # Your chat app
    "rest_framework",

]

# -------------------------------------------------------
# Middleware
# -------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

ROOT_URLCONF = "chatproject.urls"

# -------------------------------------------------------
# Templates
# -------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "chatapp" / "templates"],
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

WSGI_APPLICATION = "chatproject.wsgi.application"
ASGI_APPLICATION = "chatproject.asgi.application"

# -------------------------------------------------------
# Database (PostgreSQL)
# -------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB", "chatdb"),
        "USER": os.getenv("POSTGRES_USER", "postgres"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "2486"),
        "HOST": os.getenv("POSTGRES_HOST", "127.0.0.1"),
        "PORT": os.getenv("POSTGRES_PORT", "5432"),
    }
}

# -------------------------------------------------------
# Channels Layer (In-Memory for development)
# -------------------------------------------------------
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}

# -------------------------------------------------------
# Static files (CSS, images)
# -------------------------------------------------------
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

# -------------------------------------------------------
# Authentication
# -------------------------------------------------------
LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/chat/general/"
LOGOUT_REDIRECT_URL = "/login/"

MAX_UPLOAD_SIZE = 1024 * 1024 * 1024  # 1GB

# Media
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
