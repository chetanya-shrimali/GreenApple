from django import forms

from .models import Menu, SubMenu


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = 'category_name'


class SubMenuForm(forms.ModelForm):
    class Meta:
        model = SubMenu
        fields = ('dish_name', 'price',)
