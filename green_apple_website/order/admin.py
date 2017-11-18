from django.contrib import admin

from order.models import Order, Dish, PickUp


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'user_email', 'user_address',
                    'user_message')


class DishAdmin(admin.ModelAdmin):
    list_display = ('order', 'name')


admin.site.register(Order, OrderAdmin)
admin.site.register(Dish)
admin.site.register(PickUp)
