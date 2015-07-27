import os
from mongoengine import connect


# ------ BEGIN DON'T TOUCH AREA ------ #

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

SECRET_KEY = '{{ secret_key }}'

ROOT_URLCONF = '{{ project_name }}.urls'

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

# ------ END DON'T TOUCH AREA ------ #


DEBUG = True
DOMAIN = '<domain>'
SUBDIR = '/'  # edit this line if you are installing in a sub directory, like /libreborme
SITE_NAME = '{{ project_name }}'  # site name, you can change this

MONGO_DBNAME = 'libreborme'
MONGODB = connect(MONGO_DBNAME)

# import the default libreborme settings
# do not move this import
#from libreborme.conf.settings import *
from libreborme.settings import *


# ------ All settings customizations must go here ------ #


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Madrid'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es'

ADMINS = (
    #('Your name', 'your@email.com'),
)

MANAGERS = ADMINS

EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = 'root@localhost'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER  # used for error reporting

STATIC_ROOT = '%s/static/' % SITE_ROOT

PIWIK_URL = ''
PIWIK_SITE_ID = ''