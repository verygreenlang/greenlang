from .settings_dir.components.common import INSTALLED_APPS, MIDDLEWARE

INSTALLED_APPS.append("abstract")
MIDDLEWARE.append("simple_history.middleware.HistoryRequestMiddleware")
