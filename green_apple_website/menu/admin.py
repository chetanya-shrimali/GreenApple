from django.contrib import admin

from .models import Menu, SubMenu


class MenuAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_image')


class SubMenuAdmin(admin.ModelAdmin):
    list_display = ('menu', 'dish_name', 'price')


admin.site.register(Menu, MenuAdmin)
admin.site.register(SubMenu, SubMenuAdmin)
