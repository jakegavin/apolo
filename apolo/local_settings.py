import os
from settings import BASE_DIR

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dh#w-l6-1u2n9pr-w5zb7%gv!g$t#bu-(i_qtz+od(0#@ajirz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
