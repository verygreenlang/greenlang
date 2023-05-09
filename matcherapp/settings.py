import os
from distutils.util import strtobool
from pathlib import Path

import environ
from split_settings.tools import include, optional

env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
DEBUG = strtobool(env("DEBUG"))  # False # env("DEBUG")
ENV = env("ENV")
settings_dir = "settings_dir/"

base_settings = [
    settings_dir + "components/*.py",
    settings_dir + f"environments/{ENV}.py",
    # Optionally override some settings:
]

include(*base_settings)


#
#
#
# if DEBUG :
#     include('settings-local/*.py')
# else:
#     include('settings-prod/*.py')
