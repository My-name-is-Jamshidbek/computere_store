from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    republic = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    district_or_city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)
    apartment_number = models.CharField(max_length=10, blank=True)
    postal_code = models.CharField(max_length=10)