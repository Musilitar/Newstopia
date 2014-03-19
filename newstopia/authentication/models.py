from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class Contributor(AbstractBaseUser):
    email = models.CharField(max_length=100, primary_key=True)
    USERNAME_FIELD = 'email'