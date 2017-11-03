from django import forms

from .models import BookDetail


class BookForm(forms.ModelForm):
    class Meta:
        model = BookDetail
        fields = ('customer', 'total_persons', 'date', 'time',)
