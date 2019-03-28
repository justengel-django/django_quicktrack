# from .development import *
from .production import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!!!!!!!!!!SECRET_KEY_GOES_HERE!!!!!!!!!!'
# ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
# DEBUG = False

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATIC_URL = '/static/'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = "/media/"


# Celery
# CELERY_BROKER_URL = 'amqp://localhost'


# Email
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = ""
# EMAIL_PORT = ""
# EMAIL_HOST_USER = ""
# EMAIL_HOST_PASSWORD = ""
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = True
# EMAIL_TIMEOUT = None
# EMAIL_SSL_KEYFILE = None
# EMAIL_SSL_CERTFILE = None


# Configure Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'test_data_system_db',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': 'localhost',
#         'PORT': '',
#     },
# }

# Materialize Styling
MATERIALIZE_HIDE_CONTAINER = False
MATERIALIZE_SHOW_SIDENAV = False
MATERIALIZE_FIXED_SIDENAV = False
MATERIALIZE_PRIMARY_COLOR = 'teal'
MATERIALIZE_SECONDARY_COLOR = 'blue'
MATERIALIZE_PRIMARY_COLOR_LIGHT = None
MATERIALIZE_PRIMARY_COLOR_DARK = None
MATERIALIZE_SUCCESS_COLOR = None
MATERIALIZE_ERROR_COLOR = None
MATERIALIZE_LINK_COLOR = None

# DATETIME_INPUT_FORMATS = ['%b %d, %Y', '%B %d, %Y', '%H:%M %p', '%I:%M %p', '%b %d, %Y %H:%M %p']
