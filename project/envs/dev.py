from envs.common import *

if False:
    MIDDLEWARE_CLASSES =  (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ) + MIDDLEWARE_CLASSES

    INTERNAL_IPS = ('127.0.0.1',)

    INSTALLED_APPS += ("debug_toolbar", )