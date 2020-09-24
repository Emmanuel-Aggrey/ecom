from django import forms
from .models import Product,Sub_Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['category']

        