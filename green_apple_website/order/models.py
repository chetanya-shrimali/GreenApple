import datetime

from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50, default='customer name')
    address = models.CharField(max_length=200)
    phone_number = models.IntegerField()


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    message = models.CharField(max_length=500)


class Dish(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
