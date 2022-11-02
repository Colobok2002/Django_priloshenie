from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models



# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **fields):
        if not email:
            raise ValueError('Email is required.')

        user = self.model(
            email=UserManager.normalize_email(email),
            **fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **fields):
        fields.setdefault('is_staff', True)
        fields.setdefault('is_superuser', True)
        fields.setdefault('is_admin', True)

        return self.create_user(email=email, password=password, **fields)


class user(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        'Email',
        max_length=255,
        unique=True,
        null=False,
        blank=False
    )

    firstname = models.CharField(
        'Имя',
        max_length=40,
        null=False,
        blank=False
    )

    lastname = models.CharField(
        'Фамилия',
        max_length=40,
        null=False,
        blank=False
    )

    '''bilets = models.ManyToManyField(Bilet, default=0)
    bron = models.ManyToManyField(Bron, default=0)'''

    is_active = models.BooleanField(
        'Active',
        default=True
    )

    is_admin = models.BooleanField(
        'Is admin',
        default=False
    )

    is_staff = models.BooleanField(
        'Is staff user',
        default=False
    )

    def get_full_name(self):
        return self.firstname + " " + self.lastname

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.firstname + " " + self.lastname

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname']
    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователь'
        db_table = 'Users'
