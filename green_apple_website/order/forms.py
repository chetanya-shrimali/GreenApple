from django import forms

from order.models import Order, PickUp


class HomeForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'address', 'phone_number', 'message', 'email')


class PickUpForm(forms.ModelForm):
    class Meta:
        model = PickUp
        fields = ('name', 'contact', 'email')
