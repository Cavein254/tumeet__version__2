from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self,email=None,password=None, user_name=None,**kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,password=None, **kwargs):
        kwargs.setdefault('is_active', True)
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        if kwargs.get('is_active') is not True:
            raise ValueError('Superuser must be active')
        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must be staff')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self.create_user(email, password, **kwargs)

class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        app_label = 'users'
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects  = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['user_name']

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_user_name(self):
        return f"{self.user_name}"

    def __str__(self):
        return self.email