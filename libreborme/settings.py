"""
Django settings for libreborme project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '41+h()yq5-!*=)sh+_%4wal8=+*e)dlrau*81odpu7n&9^7d5h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ['DEBUG'] == 1 

ALLOWED_HOSTS = ['127.0.0.1', os.environ['DOMAIN']]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.postgres',
    'django.contrib.staticfiles',
    'bootstrap',
    'django_static_jquery',
    'fontawesome',
    'tastypie',
    # 'maintenancemode',
    'django_elasticsearch_dsl',
    'borme',
    'libreborme',
)


MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'maintenancemode.middleware.MaintenanceModeMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)


# if DEBUG:
#     INSTALLED_APPS += (
#         'django_extensions',
#         'debug_toolbar',
#         'elastic_panel',
#     )
#
#     DEBUG_TOOLBAR_PANELS = [
#         'debug_toolbar.panels.versions.VersionsPanel',
#         'debug_toolbar.panels.timer.TimerPanel',
#         'debug_toolbar.panels.settings.SettingsPanel',
#         'debug_toolbar.panels.headers.HeadersPanel',
#         'debug_toolbar.panels.request.RequestPanel',
#         'debug_toolbar.panels.sql.SQLPanel',
#         'elastic_panel.panel.ElasticDebugPanel',
#         'debug_toolbar.panels.staticfiles.StaticFilesPanel',
#         'debug_toolbar.panels.templates.TemplatesPanel',
#         'debug_toolbar.panels.cache.CachePanel',
#         'debug_toolbar.panels.signals.SignalsPanel',
#         'debug_toolbar.panels.logging.LoggingPanel',
#         'debug_toolbar.panels.redirects.RedirectsPanel',
#     ]
#
#     CACHES = {
#         'default': {
#             'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
#         }
#     }
#
#     MIDDLEWARE += (
#         'debug_toolbar.middleware.DebugToolbarMiddleware',
#     )


ROOT_URLCONF = 'libreborme.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'libreborme.context_processors.piwik',
                'libreborme.context_processors.common',
            ],
        },
    },
]

WSGI_APPLICATION = 'libreborme.wsgi.application'

# DEBUG
# DEBUG_TOOLBAR_CONFIG{'JQUERY_URL': '//ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js'}

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':   os.environ['LB_DB'], 'libreborme',
        'USER': os.environ['LB_USERNAME'],,
        'PASSWORD': os.environ['LB_PASSWORD'],
        'HOST': os.environ['LB_HOST'],
        'PORT': '5432',
    }
}

ELASTICSEARCH_URI = os.environ['ELASTICSEARCH_URL'],
ELASTICSEARCH_DSL = {
    'default': {
        'hosts': ELASTICSEARCH_URI.split('http://')[1]
    },
}

ELASTICSEARCH_DSL_AUTOSYNC = True
ELASTICSEARCH_DSL_AUTO_REFRESH = True

TASTYPIE_DEFAULT_FORMATS = ['json']

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

PIWIK_URL = ''
PIWIK_SITE_ID = ''

# Número de elementos a mostrar en las tablas de cargos
CARGOS_LIMIT = 20

# BORME
BORME_ROOT = os.path.expanduser('~/.bormes')
BORME_PDF_ROOT = os.path.join(BORME_ROOT, 'pdf')
BORME_XML_ROOT = os.path.join(BORME_ROOT, 'xml')
BORME_JSON_ROOT = os.path.join(BORME_ROOT, 'json')

BORME_LOG_ROOT = os.path.join(BASE_DIR, '..', 'log')

EMAIL_CONTACT = 'contact@domain'

LOPD = {'provider': 'Some real name',
        'id': 'Some real state issued ID number',
        'domain': 'The domain that hosts this website',
        'email':  EMAIL_CONTACT,
        'address': 'Some real address'}

HOST_BUCKET = "https://libreborme-prod.ams3.digitaloceanspaces.com"

INTERNAL_IPS = ('127.0.0.1')
LOGIN_URL = '/admin/login/'


STATICFILES_DIRS = (
    '/root/LibreBorme/libreborme/libreborme/static/',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

STATIC_ROOT = '/root/LibreBorme/static'

TEMPLATE_DIRS = (
    '/root/LibreBorme/libreborme/libreborme/templates/',
    '/root/LibreBorme/libreborme/borme/templates/',
)

FIXTURE_DIRS = (
    '/root/LibreBorme/libreborme/libreborme/fixtures/',
)

SECRET_KEY = '41+h()yq5-!*=)sh+_%4wal8=+*e)dlrau*81odpu7n&9^7d5h'


