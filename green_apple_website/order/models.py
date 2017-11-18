import datetime

from django.db import models


class PickUp(models.Model):
    name = models.CharField(max_length=50)
    contact = models.IntegerField(null=True)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.CharField(max_length=50, default='customer name')
    phone_number = models.IntegerField(null=True)
    user_email = models.EmailField(max_length=100, null=True)
    user_address = models.CharField(max_length=200, null=True)
    user_message = models.CharField(max_length=500, null=True)
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.user + " -> " + str(self.id)


class Dish(models.Model):
    order = models.ManyToManyField(Order)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
