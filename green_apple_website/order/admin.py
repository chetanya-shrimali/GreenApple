from django.contrib import admin

from order.models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'date', 'message', 'email')


class PickUpAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact')


# class DishAdmin(admin.ModelAdmin):
#     list_display = ('order', 'name')


admin.site.register(Order, OrderAdmin)
admin.site.register(Dish)
admin.site.register(PickUp, PickUpAdmin)
