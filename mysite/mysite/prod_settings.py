import os

DEBUG = False

# SECURE_SSL_REDIRECT = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_BROWSER_XSS_FILTER = True
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
# X_FRAME_OPTIONS = 'DENY'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# Running on production App Engine, so connect to Google Cloud SQL using
# the unix socket at /cloudsql/<your-cloudsql-connection string>
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': '/cloudsql/csx-backend:us-east1:csxdb-instance',
        'NAME': 'csxdb',
        'USER': os.environ['CSXDB_USER'],
        'PASSWORD': os.environ['CSXDB_PASSWORD']
    }
}
