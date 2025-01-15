from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#Database configuration.
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.mysql",
        "OPTIONS": {
            "read_default_file": "C:\Users\jaime\OneDrive\Escritorio\API-Recomendaciones-Musica\core\settings\my.cnf",
        },
    }
}