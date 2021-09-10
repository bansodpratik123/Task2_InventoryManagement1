from django import forms
from .models import Product

class ProductModelForm(forms.ModelForm):
    # date = forms.DateField(input_formats=['%d-%m-%Y'])
    class Meta():
        model=Product
        fields="__all__"