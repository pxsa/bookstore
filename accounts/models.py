from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomeUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)