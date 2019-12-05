from django.forms import ModelForm
from django import forms
from .models import Products, Customers


class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ['code', 'detail', 'type_product', 'packing', 'crt', 'pcs']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class CustomerForm(ModelForm):
    class Meta:
        model = Customers
        fields = ['name', 'address', 'phone']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

