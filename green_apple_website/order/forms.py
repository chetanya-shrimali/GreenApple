from django import forms

from order.models import Order, PickUp


class HomeForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('user', 'phone_number', 'user_email', 'user_address',
                  'user_message',)


class PickUpForm(forms.ModelForm):
    class Meta:
        model = PickUp
        fields = ('name', 'contact', 'email')
