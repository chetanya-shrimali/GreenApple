from django import forms

# from django.apps import apps
from .models import BookDetail


class BookForm(forms.ModelForm):
    class Meta:
        model = BookDetail
        fields = ['customer', 'contact', 'email', 'total_persons', 'date', 'time']

# class CustomerForm(forms.ModelForm):
#     class Meta:
#         model = apps.get_model('order.Customer')
#         fields = ['name', 'phone_number']
