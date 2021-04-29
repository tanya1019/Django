# to edit the profile

from django import forms
from .models import BookStore

class BookStoreForm(forms.ModelForm):
    class Meta:
        model = BookStore
        fields = ['name', 'decs', 'price', 'book_image']