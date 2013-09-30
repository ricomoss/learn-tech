from __init__ import *

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': '/home/ricomoss/workspace/python_class/'
            'track_2/apples_to_apples/apples_to_apples.db',
}
