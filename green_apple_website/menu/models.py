from django.db import models


class Menu(models.Model):
    category_name = models.CharField(max_length=100)


class SubMenu(models.Model):
    dish_name = models.CharField(max_length=100)
    price = models.IntegerField()
