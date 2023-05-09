import os
from datetime import timedelta

import environ

from .settings_dir.components.common import INSTALLED_APPS, REST_FRAMEWORK

env = environ.Env()

# Does not work with django 3.3
#
#            _           _           _                                        _
#   __ _  __| |_ __ ___ (_)_ __     | |__   ___  _ __   ___ _   _ _ __   ___ | |_
#  / _` |/ _` | '_ ` _ \| | '_ \    | '_ \ / _ \| '_ \ / _ \ | | | '_ \ / _ \| __|
# | (_| | (_| | | | | | | | | | |   | | | | (_) | | | |  __/ |_| | |_) | (_) | |_
#  \__,_|\__,_|_| |_| |_|_|_| |_|___|_| |_|\___/|_| |_|\___|\__, | .__/ \___/ \__|
#                              |_____|                      |___/|_|
# INSTALLED_APPS.append('admin_honeypot')

#
#      ___        _______
#     | \ \      / /_   _|
#  _  | |\ \ /\ / /  | |
# | |_| | \ V  V /   | |
#  \___/   \_/\_/    |_|

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
}

INSTALLED_APPS.append("rest_framework_simplejwt")
INSTALLED_APPS.append("rest_framework.authtoken")

REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"].append(
    "rest_framework_simplejwt.authentication.JWTAuthentication"
)


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": env("SECRET_KEY"),
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "JWK_URL": None,
    "LEEWAY": 0,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}


# Djose

INSTALLED_APPS.append("djoser")

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
DJOSER = {
    "PASSWORD_RESET_CONFIRM_URL": "app/resetpassword/{uid}/{token}",
    "USERNAME_RESET_CONFIRM_URL": "app/resetpassword/{uid}/{token}",
    "ACTIVATION_URL": "#/activate/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": False,
    "CREATE_SESSION_ON_LOGIN": True,
    "LOGIN_FIELD": "email",
}



#  ____   _    ____ ______        _____  ____  ____  _     _____ ____ ____
# |  _ \ / \  / ___/ ___\ \      / / _ \|  _ \|  _ \| |   | ____/ ___/ ___|
# | |_) / _ \ \___ \___ \\ \ /\ / / | | | |_) | | | | |   |  _| \___ \___ \
# |  __/ ___ \ ___) |__) |\ V  V /| |_| |  _ <| |_| | |___| |___ ___) |__) |
# |_| /_/   \_\____/____/  \_/\_/  \___/|_| \_\____/|_____|_____|____/____/
#

# django password less
# INSTALLED_APPS.append("drfpasswordless")
# REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"].append(
#     "rest_framework.authentication.TokenAuthentication"
# )
# #
# PASSWORDLESS_AUTH = {
#     # Allowed auth types, can be EMAIL, MOBILE, or both.
#     "PASSWORDLESS_AUTH_TYPES": ["EMAIL"],
#     # URL Prefix for Authentication Endpoints
#     "PASSWORDLESS_AUTH_PREFIX": "auth/",
#     #  URL Prefix for Verification Endpoints
#     "PASSWORDLESS_VERIFY_PREFIX": "auth/verify/",
#     # Amount of time that tokens last, in seconds
#     "PASSWORDLESS_TOKEN_EXPIRE_TIME": 15 * 60,
#     # The user's email field name
#     "PASSWORDLESS_USER_EMAIL_FIELD_NAME": "email",
#     # The user's mobile field name
#     "PASSWORDLESS_USER_MOBILE_FIELD_NAME": "mobile",
#     # Marks itself as verified the first time a user completes auth via token.
#     # Automatically unmarks itself if email is changed.
#     "PASSWORDLESS_USER_MARK_EMAIL_VERIFIED": False,
#     "PASSWORDLESS_USER_EMAIL_VERIFIED_FIELD_NAME": "email_verified",
#     # Marks itself as verified the first time a user completes auth via token.
#     # Automatically unmarks itself if mobile number is changed.
#     "PASSWORDLESS_USER_MARK_MOBILE_VERIFIED": False,
#     "PASSWORDLESS_USER_MOBILE_VERIFIED_FIELD_NAME": "mobile_verified",
#     # The email the callback token is sent from
#     "PASSWORDLESS_EMAIL_NOREPLY_ADDRESS": None,
#     # The email subject
#     "PASSWORDLESS_EMAIL_SUBJECT": "Your Login Token",
#     # A plaintext email message overridden by the html message. Takes one
#     # string.
#     "PASSWORDLESS_EMAIL_PLAINTEXT_MESSAGE": "Enter this token to sign in: %s",
#     # The email template name.
#     "PASSWORDLESS_EMAIL_TOKEN_HTML_TEMPLATE_NAME": "passwordless_default_token_email.html",
#     # Your twilio number that sends the callback tokens.
#     "PASSWORDLESS_MOBILE_NOREPLY_NUMBER": None,
#     # The message sent to mobile users logging in. Takes one string.
#     "PASSWORDLESS_MOBILE_MESSAGE": "Use this code to log in: %s",
#     # Registers previously unseen aliases as new users.
#     "PASSWORDLESS_REGISTER_NEW_USERS": True,
#     # Suppresses actual SMS for testing
#     "PASSWORDLESS_TEST_SUPPRESSION": False,
#     # Context Processors for Email Template
#     "PASSWORDLESS_CONTEXT_PROCESSORS": [],
#     # The verification email subject
#     "PASSWORDLESS_EMAIL_VERIFICATION_SUBJECT": "Your Verification Token",
#     # A plaintext verification email message overridden by the html message.
#     # Takes one string.
#     "PASSWORDLESS_EMAIL_VERIFICATION_PLAINTEXT_MESSAGE": "Enter this verification code: %s",
#     # The verification email template name.
#     "PASSWORDLESS_EMAIL_VERIFICATION_TOKEN_HTML_TEMPLATE_NAME": "passwordless_default_verification_token_email.html",
#     # The message sent to mobile users logging in. Takes one string.
#     "PASSWORDLESS_MOBILE_VERIFICATION_MESSAGE": "Enter this verification code: %s",
#     # Automatéically send verification email or sms when a user changes their
#     # alias.
#     "PASSWORDLESS_AUTO_SEND_VERIFICATION_TOKEN": False,
#     # What function is called to construct an authentication tokens when
#     # exchanging a passwordless token for a real user auth token. This function
#     # should take a user and return a tuple of two values. The first value is
#     # the token itself, the second is a boolean value representating whether
#     # the token was newly created.
#     "PASSWORDLESS_AUTH_TOKEN_CREATOR": "drfpasswordless.utils.create_authentication_token",
#     # What function is called to construct a serializer for drf tokens when
#     # exchanging a passwordless token for a real user auth token.
#     "PASSWORDLESS_AUTH_TOKEN_SERIALIZER": "drfpasswordless.serializers.TokenResponseSerializer",
#     # A dictionary of demo user's primary key mapped to their static pin
#     "PASSWORDLESS_DEMO_USERS": {},
#     # configurable function for sending email
#     "PASSWORDLESS_EMAIL_CALLBACK": "drfpasswordless.utils.send_email_with_callback_token",
#     # configurable function for sending sms
#     "PASSWORDLESS_SMS_CALLBACK": "drfpasswordless.utils.send_sms_with_callback_token",
#     # Token Generation Retry Count
#     "PASSWORDLESS_TOKEN_GENERATION_ATTEMPTS": 3,
# }
