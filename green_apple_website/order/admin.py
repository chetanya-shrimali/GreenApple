from django.contrib import admin

from order.models import Order, Dish, PickUp


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'address', 'phone_number', 'date', 'message', 'email')


class DishAdmin(admin.ModelAdmin):
    list_display = ('order', 'name')


admin.site.register(Order, OrderAdmin)
admin.site.register(Dish)
admin.site.register(PickUp)
