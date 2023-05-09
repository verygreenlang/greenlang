from .settings_dir.components.common import BASE_DIR

STATIC_URL = "static/"
STATIC_ROOT="static/"
# DJANGO_SUPERUSER_PASSWORD="greenfin"
# DJANGO_SUPERUSER_EMAIL="cto@fingreen.ai"
# DJANGO_SUPERUSER_USERNAME="cto"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
PRIVATE_STORAGE_ROOT = 'private-media/'
#PRIVATE_STORAGE_AUTH_FUNCTION =  'custom_auth.permissions.allow_same_team'
#'private_storage.permissions.allow_authenticated'
