from django.contrib.auth.models import UserManager as DjangoUserManager
from django.db import models
from parent_app import models as parent_app_models


class UserManager(DjangoUserManager):
    use_in_migrations = False

    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = queryset.prefetch_related(models.Prefetch('items', queryset=Item.objects.all()))

        return queryset


class User(parent_app_models.User):
    user_ptr = models.OneToOneField(to='parent_app.user', related_name="child_app_user", on_delete=models.CASCADE, parent_link=True, primary_key=True, serialize=False)
    objects = UserManager()


class Item(models.Model):
    users = models.ManyToManyField('User', related_name='items', blank=True)
    description = models.CharField(max_length=400)
    quantity = models.IntegerField(default=0)
