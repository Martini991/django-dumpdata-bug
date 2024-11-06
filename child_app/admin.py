from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from child_app import models

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Item, admin.ModelAdmin)
