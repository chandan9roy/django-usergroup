import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


DEBUG = True
TEMPLATE_DEBUG = DEBUG
DEBUG_PROPAGATE_EXCEPTIONS = DEBUG
 
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = ':memory:'

TIME_ZONE = 'UTC'
    
SITE_ID = 1
      
SECRET_KEY = '00000000000000000000000000000000000000000000000000'

ROOT_URLCONF = 'example.urls'

TEMPLATE_DIRS = (
    os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'usergroups',
    'example.groups',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite1'),
    }
}


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)