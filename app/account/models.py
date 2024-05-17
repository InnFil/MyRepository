from django.utils import timezone

from account.managers import UserManager
from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    username = models.TextField(verbose_name='Имя пользователя', unique=True)
    email = models.EmailField(verbose_name='Электронная почта')
    phone = models.CharField(verbose_name='Номер телефона')

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone']

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        unique_together = ('username', 'email', 'phone')


class LoginCode(models.Model):
    phone_number = models.CharField(verbose_name='Номер телефона')
    code = models.IntegerField(verbose_name='Код')
    create_at = models.DateTimeField(verbose_name='Дата и время создания', auto_now_add=True)
