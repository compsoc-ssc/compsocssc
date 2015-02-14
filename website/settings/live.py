from django.conf import settings
DATABASES=settings.DATABASES
DEBUG=False
TEMPLATE_DEBUG=DEBUG
#for heroku
# Parse database configuration from $DATABASE_URL
#import dj_database_url
#DATABASES['default'] = dj_database_url.config()
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# Allow all host headers
ALLOWED_HOSTS = ['*']
#domain_name='http://testssc.pythonanywhere.com:80'
