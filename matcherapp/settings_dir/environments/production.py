import os

import environ

from .settings_dir.components.common import INSTALLED_APPS, REST_FRAMEWORK

REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = [
    "rest_framework.renderers.JSONRenderer",
]

INSTALLED_APPS.append("storages")
INSTALLED_APPS.append("private_storage")

AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ[
     "AWS_SECRET_ACCESS_KEY"
 ]
AWS_STORAGE_BUCKET_NAME = os.environ["AWS_STORAGE_BUCKET_NAME"]
AWS_S3_REGION_NAME = os.environ["AWS_S3_REGION_NAME"]
AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
#
# AWS_S3_OBJECT_PARAMETERS = {
#     "CacheControl": "max-age=86400",
# }
#
AWS_STATIC_LOCATION = "static"
#STATICFILES_STORAGE = "storage.file_s3.StaticStorage"
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_STATIC_LOCATION}/"

AWS_DEFAULT_ACL = 'public-read'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
AWS_LOCATION = 'static'

# AWS_PUBLIC_MEDIA_LOCATION = "media/public"
# DEFAULT_FILE_STORAGE = "storage.file_s3.PublicMediaStorage"
#
# AWS_PRIVATE_MEDIA_LOCATION = "media/private"
# PRIVATE_FILE_STORAGE = "storage.file_s3.PrivateMediaStorage"
#
# PRIVATE_STORAGE_ROOT = "media/private"
# # PRIVATE_STORAGE_AUTH_FUNCTION = "private_storage.permissions.allow_staff"
# # PRIVATE_STORAGE_AUTH_FUNCTION = 'custom_auth.permissions.allow_same_team'
# # PRIVATE_STORAGE_AUTH_FUNCTION = 'private_storage.permissions.allow_authenticated'
# #PRIVATE_STORAGE_AUTH_FUNCTION =  'custom_auth.permissions.allow_same_team'
#
# PRIVATE_STORAGE_CLASS = "private_storage.storage.s3boto3.PrivateS3BotoStorage"
#
# AWS_PRIVATE_STORAGE_BUCKET_NAME = os.environ["AWS_PRIVATE_STORAGE_BUCKET_NAME"]
# AWS_PRIVATE_QUERYSTRING_AUTH = False


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ["RDS_DB_NAME"],
        "USER": os.environ["RDS_USERNAME"],
        "PASSWORD": os.environ["RDS_PASSWORD"],
        "HOST": os.environ["RDS_HOSTNAME"],
        "PORT": os.environ["RDS_PORT"],
    }
}


# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "handlers": {
#         "file": {
#             "level": "DEBUG",
#             "class": "logging.FileHandler",
#             "filename": "/var/log/eb-django.log",
#         },
#     },
#     "loggers": {
#         "django": {
#             "handlers": ["file"],
#             "level": "DEBUG",
#             "propagate": True,
#         },
#     },
# }
