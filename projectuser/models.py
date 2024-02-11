from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=150)
    phoneno = models.CharField(max_length=200)
    first_name = models.CharField()
    last_name = models.CharField()
    

    def __str__(self):
        return self.username