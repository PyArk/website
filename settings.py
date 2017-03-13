FLASK_DEBUG = True
FLASK_HOST = 'localhost'
FLASK_PORT = 5000
SITE_NAME = 'Python User Group of Central Arkansas'
ADMIN_EMAIL = 'info@example.com'
ERROR_EMAIL = 'info+errors@example.com' 
ASSETS_DEBUG = FLASK_DEBUG
MEETUP_SLUG = 'Python-Artists-of-Arkansas'

try:
    from local_settings import *
except ImportError:
    pass
