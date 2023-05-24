from .base import ALLOWED_HOSTS, DEBUG, SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = DEBUG

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ALLOWED_HOSTS

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# INSTALLED_APPS = INSTALLED_APPS + [
#     "debug_toolbar",
# ]

# MIDDLEWARE = MIDDLEWARE + [
#     "debug_toolbar.middleware.DebugToolbarMiddleware",
# ]

INTERNAL_IPS = ("127.0.0.1", "172.17.0.1")
