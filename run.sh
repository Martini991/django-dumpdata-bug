# python3.12 -m venv .venv
# pip install django==5.1.3

source .venv/bin/activate

export DJANGO_SETTINGS_MODULE=wrong_user_manager.settings
export PYTHONPATH="${PWD}"
export PYTHONDONTWRITEBYTECODE=1
export PYTHONUNBUFFERED=1

django-admin migrate
django-admin runserver 0.0.0.0:80
