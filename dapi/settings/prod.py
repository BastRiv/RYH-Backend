from .settings import *


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'hiredone01db',
    'USER': 'hiredoneuserpsql',
    'PASSWORD': 'Hire2021DB01++$$',
    'HOST': 'localhost',
    'PORT': '5432',
    }
}



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR.child('static')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')



# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'es-cl'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

