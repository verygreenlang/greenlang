import os

import boto3
import environ
from botocore.config import Config

from .settings_dir.components.common import INSTALLED_APPS, REST_FRAMEWORK

env = environ.Env()

#
#
# ANYMAIL = {
#     # (exact settings here depend on your ESP...)
#     "MAILGUN_API_KEY": "<your Mailgun key>",
#     "MAILGUN_SENDER_DOMAIN": 'fingreen.ai',  # your Mailgun domain, if needed
# }
# EMAIL_BACKEND = "anymail.backends.amazon_ses.EmailBackend"  # or sendgrid.EmailBackend, or...
# DEFAULT_FROM_EMAIL = "you@fingreen.co"  # if you don't already have this in settings
# SERVER_EMAIL = "server@fingreen.co"
INSTALLED_APPS.append("django_ses")
EMAIL_BACKEND = "django_ses.SESBackend"


env = environ.Env()

my_config = Config(
    region_name="us-west-3",
    signature_version="v4",
    retries={"max_attempts": 10, "mode": "standard"},
)


AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")  # 'AKIAIT2Z5TDYPX3ARJBA'
AWS_SECRET_ACCESS_KEY = env(
    "AWS_SECRET_ACCESS_KEY"
)  # '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'
# 'django-wealth-manager-app'
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME")
os.environ["AWS_DEFAULT_REGION"] = env("AWS_S3_REGION_NAME")
AWS_SES_REGION_NAME = env("AWS_SES_REGION_NAME")
AWS_SES_REGION_ENDPOINT = env(
    "AWS_SES_REGION_ENDPOINT"
)  # 'email.us-west-2.amazonaws.com'


#
# EMAIL_HOST = env('EMAIL_HOST')
# EMAIL_HOST_USER = env('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
