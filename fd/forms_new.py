from django import forms
from .models import Products

class ProductForm(forms.Form):
    code = forms.CharField(label='Code', max_length=20, required=True)
    detail = forms.CharField(label='Detail', max_length=20)
    type_product = forms.CharField(label='Type', max_length=20)
    packing = forms.CharField(label='Packing', max_length=20)
    crt = forms.CharField(label='Crt', max_length=20)
    pcs = forms.CharField(label='Pcs', max_length=20)