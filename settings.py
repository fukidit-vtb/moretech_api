import logging
import os
from datetime import datetime

from envparse import Env, shortcut

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

env = Env()
env.read_envfile(os.path.join(BASE_DIR, '.env'))

datetime_str = shortcut(lambda s: datetime.fromisoformat(s))

try:
    env.read_envfile()
except Exception as e:
    logging.warning(e)

DEFAULT_HOST = '0.0.0.0'

SERVICE_NAME = 'MORETECH_FUKIDID'
ENVIRONMENT = env.str('ENVIRONMENT', default='dev')
HOST = env.str('HOST', default=DEFAULT_HOST)
PORT = env.int('PORT', default=8089)
DEBUG = env.bool('DEBUG', default=False)
