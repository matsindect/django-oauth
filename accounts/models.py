from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
from datetime import datetime

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_superuser=False):
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("User must have an passwords")
        user_obj = self.model(
            email= self.normalize_email(email)
        )

        user_obj.set_password(password)
        user_obj.is_member= is_staff
        user_obj.is_admin= is_superuser
        user_obj.active= is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user= self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, password=None):
        user= self.create_user(
            email,
            password=password,
            is_staff=True,
            is_superuser=True
        )

        return user


# Create your models here.
class User(AbstractBaseUser):
    email= models.EmailField(max_length=255, unique=True)
    active= models.BooleanField(default= True) # can login
    is_member= models.BooleanField(default=False) # member
    is_admin = models.BooleanField(default=False) # superuser
    timestamp= models.DateField(auto_now_add=True)
    confirmed_email= models.BooleanField(default=False)

    USERNAME_FIELD='email' # change username to email
    
    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_member

    @property
    def is_superuser(self):
        return self.is_admin