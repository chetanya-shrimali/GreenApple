from django.contrib import admin

from order.models import Order, Dish


class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'date', 'message')


# class DishAdmin(admin.ModelAdmin):
#     list_display = ('order', 'name')


admin.site.register(Order, OrderAdmin)
admin.site.register(Dish)
