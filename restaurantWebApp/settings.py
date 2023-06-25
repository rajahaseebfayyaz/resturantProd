"""
Django settings for restaurantWebApp project by @rajaSaheebFayyaz.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""


import os
if os.path.isfile("env.py"):
    import env

from pathlib import Path


import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

"""
    @rajaSaheebFayyaz.
    Reading the secret key from environmet variable, instead of hardcoded value.
"""


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =   os.environ.get("SECRET_KEY") #os.environ['SECRET_KEY'] #'o+un^+_hcls)sl2dv$9ul8sfg!c0k1a&e@)7(3uknhgzbz_7@w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["restaurantWebApp.herokuapp.com", "localhost"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admindocs',
    'cloudinary',
    'django.contrib.staticfiles',
    'cloudinary_storage',

    
    # @rajaSaheebFayyaz. Registering Apps used in the project
       

    # Registered the home page App.
    'home',
    # Registered the meals page App.
    'meals',
    # Registered the blogs page App.
    'blog',
    # Registered the contact page App.
    'contact',
    # Registered the aboutus page App.
    'aboutus',
    # Registered the reservation page App.
    'reservation',

    # installed libs
    'taggit',
    'bootstrap4',
    'django_summernote',
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

ROOT_URLCONF = 'restaurantWebApp.urls'

TEMPLATES_DIR = os.path.join(BASE_DIR,'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'restaurantWebApp.wsgi.application'


"""
    @rajaHaseebFayyaz
    Un comment the below mentioned database info, to use external database
    and change the field acc. to new configuration of database.
"""

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
# DATABASES = {
# 'default': {
#     'ENGINE': 'django.db.backends.postgresql_psycopg2',
#     'NAME': 'resturantly',
#     'USER': 'postgres',
#     'PASSWORD': 'root',
#     'HOST': 'localhost',
#     'PORT': '5432',
# }
# }
# print("dsdsdsds/n",os.environ("DATABSE_URL"))
# exit()
DATABASES = {
'default':
dj_database_url.parse(os.environ.get("DATABSE_URL"))
}

"""
    @rajaSaheebFayyaz.
    Self contained databased for development environment.
"""

# DATABASES is a dictionary of database names mapped to a dictionary of settings that can be used to configure the database
# DATABASES = {
# 'default': {
# 'ENGINE': 'django.db.backends.sqlite3',
# 'NAME': BASE_DIR / 'db.sqlite3',
# }
# }





# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE ='cloudinary_storage.storage.MediaCloudinaryStorage'


"""
    @rajaSaheebFayyaz.
    Register the media folder to locate media files globally used in project.
"""
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False