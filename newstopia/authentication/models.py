from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class ContribManager(BaseUserManager):
    def create_user(self, email,
                    password=None):
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email,
                    password=None):
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

class Contributor(AbstractBaseUser):
    email = models.CharField(max_length=100, primary_key=True)
    USERNAME_FIELD = 'email'
    objects = ContribManager()