# This is an example test settings file for use with the Django test suite.
#
# The 'sqlite3' backend requires only the ENGINE setting (an in-
# memory database will be used). All other backends will require a
# NAME and potentially authentication information. See the
# following section in the docs for more information:
#
# https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/
#
# The different databases that Django supports behave differently in certain
# situations, so it is recommended to run the test suite against as many
# database backends as possible.  You may want to create a separate settings
# file for each of the backends you test against.

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'USER': 'django',
        'PASSWORD': 'django',
        'NAME': 'django',
        'HOST': 'postgres-gis-db'
    },
    'other': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'USER': 'django',
        'NAME': 'django2',
        'PASSWORD': 'django',
        'HOST': 'postgres-gis-db'
    }
}

SECRET_KEY = "django_tests_secret_key"

# Use a fast hasher to speed up tests.
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

GEOIP_PATH = '/geolite2/'

TEST_RUNNER = 'xmlrunner.extra.djangotestrunner.XMLTestRunner'
TEST_OUTPUT_DIR = '/tests/results'
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
USE_TZ = False
