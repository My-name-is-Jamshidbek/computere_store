from django.db import models

class Installment(models.Model):
    name = models.CharField(max_length=255)
    months = models.PositiveIntegerField()
    percentage = models.PositiveIntegerField()
    minimum_money = models.PositiveIntegerField()
    maximum_money = models.PositiveIntegerField()

