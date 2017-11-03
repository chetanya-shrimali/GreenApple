from django.db import models


class Menu(models.Model):
    category_name = models.CharField(max_length=100,
                                     default='enter menu category')

    def __str__(self):
        return self.category_name


class SubMenu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    dish_name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.menu.category_name + ' -> ' + self.dish_name
