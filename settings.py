FLASK_DEBUG = True
SITE_NAME = 'Python Artist of Arkansas'
ADMIN_EMAIL = 'info@example.com'
ERROR_EMAIL = 'info+errors@example.com' 
ASSETS_DEBUG = FLASK_DEBUG
MEETUP_SLUG = 'Python-Artists-of-Arkansas'

try:
    from local_settings import *
except ImportError:
    pass
