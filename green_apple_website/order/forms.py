from django import forms

from .models import Customer, OrderDetail, Order


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'address', 'phone_number',)


# class OrderForm(forms.ModelForm)
#     class Meta:
#         model = Order
#         fields = ('total_price', )
#

# class OrderDetailForm(forms.ModelForm):
#     class Meta:
#         model = OrderDetail
#         fields = ('selected_item', 'quantity', 'price')

