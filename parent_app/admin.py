from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from parent_app import models

admin.site.register(models.User, UserAdmin)
