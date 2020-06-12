"""
Django settings for memorymap_toolkit project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from unipath import Path

BASE_DIR = Path(__file__).ancestor(2)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xc0#odq6lq^ghf_s_x5gu+17(uzzm1gva@-47+f%^s4&_9dc90'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    # Constance
    'constance.backends.database',
    # Memory Map Toolkit
    'mmt_map',
    'mmt_pages',
    'mmt_api',
    # 3rd Party
    'easy_thumbnails',
    'filer',
    'mptt',
    'ckeditor',
    'ckeditor_uploader',
    'constance',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'memorymap_toolkit.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.child('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'memorymap_toolkit.context_processors.site_settings'
            ],
        },
    },
]

WSGI_APPLICATION = 'memorymap_toolkit.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'HOST': 'localhost',
        'NAME': 'memorymap_toolkit',
        'USER': 'memorymap_toolkit',
        'PASSWORD': 'memorymap_toolkit'
    }
}


# Caching. The dynamically-created map tiles are cached using memcached so the load on the database isn't too heavy for larger interactive maps

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR.child('static')

STATICFILES_DIRS = [
    BASE_DIR.child('project_static'),
]

# Media Settings

MEDIA_ROOT = BASE_DIR.child('media')
MEDIA_URL = '/media/'



### App-Specific Settings ###

# Django-ckeditor Settings

CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Format', 'Bold', 'Italic', 'Underline'],
            ['BulletedList', 'Blockquote'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Flash', 'Table', 'HorizontalRule', 'SpecialChar'],
            ['RemoveFormat', 'Source']
        ]
    },
}

# Easy Thumbnails

THUMBNAIL_ALIASES = {
    '': {
        'site_small': {'size': (300, 175), 'crop': 'smart', 'upscale': True},
        'banner': {'size': (600, 350), 'crop': 'smart', 'upscale': True},
    },
}

# Constance

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

CONSTANCE_CONFIG = {
    'SITE_TITLE': ('Memory Map Toolkit', 'The name of your site'),
    'MAP_CENTER_LATITUDE': (0.0, 'The latitude of the centre point of the map'),
    'MAP_CENTER_LONGITUDE': (0.0, 'The longitude of the centre point of the map'),
    'ZOOM': (15.5, 'The default zoom level of the map'),
    'MIN_ZOOM': (9.5, 'The lowest zoom level of the map'),
    'MAX_ZOOM': (18.4, 'The highest zoom level of the map'),
    'BASE_MAP_STYLE': ('/static/js/default_map_style.json', 'URL to a MapboxGL Map style'),
    'BASE_MAP_STYLE_KEY': ('', 'The default map style uses Ordnance Survey Open Zoomstack tiles hosted with Maptiler Cloud. To use these, you need to sign up for a free account and copy your user key here'),
    'SCALE': ('metric', 'The units to use for the map scale widget'),
    'PITCH': (0, 'The pitch of the map viewport'),
    'BEARING': (0, 'The bearing of the map viewport'),
    'WELCOME_MESSAGE': ('Welcome to the Memory Map Toolkit', 'The message that displays when the site loads'),
    'SITE_METADATA': ('', 'Metadata in json-ld format. Adding this will improve the visibility of your site in search results'),
    'SWITCHABLE_LAYERS': ('', 'A comma-separated list of map layer IDs from your map style definition. This will allow visitors to your site to switch layers on and off from the menu bar. Particularly useful if you are using historic maps.'),
}




### Memory Map Toolkit Settings ###

SITE_TITLE = 'Memory Map Toolkit'

MAP_CENTER = {'lat': 54.047220, 'lon': -2.904659}

ZOOM = 15.5

MIN_ZOOM = 9.5

MAX_ZOOM = 18.4

MAX_BOUNDS = []

SCALE = 'metric'

BASE_MAP_STYLE = None

PITCH = 0

BEARING = 0

BASE_MAP_SOURCE = {
    'Ordnance Survey Open Zoomstack': {
        'title': 'Ordnance Survey Open Zoomstack',
        'url': 'https://api.maptiler.com/tiles/uk-openzoomstack/tiles.json?key=fL9NKV06gTKowpkIEnt4',
        'attribution': '',
        'type': 'vector'
    }
}

RASTER_SOURCES = [
    {
        'title': '',
        'url': '',
        'attribution': '',
        'raster_saturation': 0,
        'raster_contrast': 0,
        'raster_brightness_min': 0,
        # Set raster opacity to 0 to hide layer on load.
        'raster_opacity': 0
    }
]

VECTOR_SOURCES = [
    { 
        'title': 'Ordnance Survey Open Zoomstack',
        'url': 'https://api.maptiler.com/tiles/uk-openzoomstack/tiles.json?key=fL9NKV06gTKowpkIEnt4',
        'attribution': '',
        'type': 'vector'
    }
]

ALLOWED_HOSTS = []

WELCOME_MESSAGE = """
    <p>Put your site welcome message here.</p>
"""

# Add schema.org metadata here in json-ld format to improve the visibility of your site in search results

SITE_METADATA = """
{
    "@context": "http://schema.org",
    "@type": "WebSite",
    "url": "https://jewisheastendmemorymap.org/",
    "author": {
        "@context": "http://schema.org",
        "@type": "EducationalOrganization",
        "name": "University College London",
        "address": {
            "@context": "http://schema.org",
            "@type": "PostalAddress",
            "addressCountry": "United Kingdom",
            "addressLocality": "London",
            "postalCode": "EC1N 2ST",
            "streetAddress": "Gower Street, London"
        }
    },
    "about": {
        "@context": "http://schema.org",
        "@type": "Place",
        "name": "Whitechapel"
    },
    "description": "A Memory Map of the Jewish East End. Find interviews, photographs, and essays about this now-vanished territory."
}
"""

