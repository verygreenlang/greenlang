from .settings_dir.components.common import INSTALLED_APPS, REST_FRAMEWORK

REST_FRAMEWORK["TEST_REQUEST_DEFAULT_FORMAT"] = "json"
REST_FRAMEWORK["TEST_REQUEST_RENDERER_CLASSES"] = [
    "rest_framework.renderers.MultiPartRenderer",
    "rest_framework.renderers.JSONRenderer",
    "rest_framework.renderers.TemplateHTMLRenderer",
]
