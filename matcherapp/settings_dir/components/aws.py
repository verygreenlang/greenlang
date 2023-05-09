# import boto3
# from botocore.config import Config
# import environ,os
# env = environ.Env()
#
# my_config = Config(
#     region_name = 'us-west-3',
#     signature_version = 'v4',
#     retries = {
#         'max_attempts': 10,
#         'mode': 'standard'
#     }
# )
#
#
# AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")# 'AKIAIT2Z5TDYPX3ARJBA'
# AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY") #'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'
# AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")#'django-wealth-manager-app'
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
#
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }
#
# AWS_STATIC_LOCATION = 'static'
# STATICFILES_STORAGE = 'storage.file_s3.StaticStorage'
# STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)
#
# AWS_PUBLIC_MEDIA_LOCATION = 'media/public'
# DEFAULT_FILE_STORAGE ='storage.file_s3.PublicMediaStorage'
#
# AWS_PRIVATE_MEDIA_LOCATION = 'media/private'
# PRIVATE_FILE_STORAGE = 'storage.file_s3.PrivateMediaStorage'
