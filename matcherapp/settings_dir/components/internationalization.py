import environ

env = environ.Env()

LANGUAGE_CODE = env("LANGUAGE_CODE")  # 'en-us'

TIME_ZONE = env("TIME_ZONE")  # 'UTC'

USE_I18N = env("USE_I18N")

USE_TZ = env("USE_TZ")  # True
