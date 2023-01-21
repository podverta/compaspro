from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import UserManager


class UserMy(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True, blank=True)
    email = models.EmailField('Email', unique=True)
    role_in_choices = [
        ('Пользователь', 'Пользователь'),
        ('Менеджер', 'Менеджер'),
        ('CRM-администратор', 'CRM-администратор'),
    ]
    role_choice = models.CharField('Role', max_length=40,
                                   choices=role_in_choices)
    offer = models.BooleanField(default=False)
    avatar = models.ImageField(
        default='media/user.png',
        blank=True,
        null=False,
    )
    #для админки
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'role_choice', 'offer']

    objects = UserManager()


    def __str__(self):
        return self.username