from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User
from django.utils import timezone

# Create your models here.
class User(AbstractBaseUser):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    hr = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    warehoue = models.BooleanField(default=False)
    supervisor = models.BooleanField(default=False)
    ismanager = models.BooleanField(default=False)
    customer = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)


# class UserRole(models.Model):
#     usr = models.ForeignKey(User, on_delete=models.CASCADE)
#     supervisor = models.BooleanField(default=False)
#     ismanager = models.BooleanField(default=False)
#     customer = models.BooleanField(default=False)