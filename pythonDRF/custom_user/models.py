from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Phone(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.phone_number