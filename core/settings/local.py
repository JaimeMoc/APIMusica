from .base import *

#Database configuration.
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.mysql",
        "OPTIONS": {
            "read_default_file": r"C:\Users\jaime\OneDrive\Escritorio\API-Recomendaciones-Musica\core\settings\my.cnf",
        },
    }
}