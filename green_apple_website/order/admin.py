from django.contrib import admin

from .models import Customer, Order, Dish

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Dish)
