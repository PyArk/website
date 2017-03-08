FLASK_DEBUG = True
SITE_NAME = 'PYAR2: Python Artist of Arkansas'
ADMIN_EMAIL = 'info@example.com' # TODO add real email address
ASSETS_DEBUG = FLASK_DEBUG
MEETUP_SLUG = 'Python-Artists-of-Arkansas'

try:
    from local_settings import *
except ImportError:
    pass
