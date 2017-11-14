from django.contrib import admin

from .models import Customer, Order, Dish


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'date', 'message')


class DishAdmin(admin.ModelAdmin):
    list_display = ('order', 'name')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Dish, DishAdmin)
