import datetime

from django.db import models


class PickUp(models.Model):
    name = models.CharField(max_length=50)
    contact = models.IntegerField(null=True)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=50, default='customer name')
    address = models.CharField(max_length=200, null=True)
    phone_number = models.IntegerField(null=True)
    date = models.DateField(default=datetime.date.today)
    message = models.CharField(max_length=500, null=True)
    email = models.EmailField(max_length=100, null=True)

    def __str__(self):
        return self.name + " -> " + str(self.id)


class Dish(models.Model):
    order = models.ManyToManyField(Order)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
