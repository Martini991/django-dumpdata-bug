from django.core.wsgi import get_wsgi_application
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wrong_user_manager.settings')
application = get_wsgi_application()
