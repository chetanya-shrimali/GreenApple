from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone_number = models.IntegerField(max_length=15)


class Order(models.Model):
    total_price = models.IntegerField(max_length=10)
    total_items = models.IntegerField(max_length=10)
    message = models.CharField(max_length=500)


class OrderDetail(models.Model):
    selected_item = models.CharField(max_length=50)
    quantity = models.IntegerField(max_length=10)
    price = models.IntegerField(max_length=10)
