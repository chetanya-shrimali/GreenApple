from django.db import models


class Menu(models.Model):
    customer = models.ForeignKey('order.Customer', on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100, default='enter menu category')


class SubMenu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    dish_name = models.CharField(max_length=100)
    price = models.IntegerField()
