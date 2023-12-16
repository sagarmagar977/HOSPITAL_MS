from django.db import models
from django.contrib.auth.models import AbstractUser

class user(AbstractUser):
    username=models.CharField(max_length=100,null=True,default='user')
    email=models.EmailField(unique=True,max_length=100)
    password=models.CharField(max_length=300)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

# Create your models here.
