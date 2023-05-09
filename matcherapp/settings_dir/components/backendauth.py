import environ

env = environ.Env()

BACKEND_SUPER_USER = env("BACKEND_SUPER_USER")  # 'en-us'

BACKEND_PASSWORD = env("BACKEND_PASSWORD")  # 'UTC'
