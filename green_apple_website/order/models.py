import datetime

from django.core.validators import MaxValueValidator
from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=50, default='customer name')
    address = models.CharField(max_length=200, null=True)
    phone_number = models.PositiveIntegerField(null=True, validators=[MaxValueValidator(9999999999)])
    date = models.DateField(default=datetime.date.today)
    message = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name + " -> " + str(self.id)


class Dish(models.Model):
    order = models.ManyToManyField(Order)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
