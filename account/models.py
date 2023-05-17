from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(verbose_name='email', max_length=100, blank=True, null=True, unique=True)
    nickname = models.CharField(max_length=30, blank=True, null=True)
    profile = models.CharField(max_length=256, default='default_profile.jpg', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.nickname

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = 'users'


