from dal import autocomplete
from django.forms import ModelForm, TextInput, HiddenInput
from django import forms
from .models import Products, Customers, Transaction, Detail_transaction


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
        widgets = {
            'name': TextInput(),
            'phone':TextInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class SuratJalanForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['customers_name', 'transaction_date']
        widgets = {
            'customers_name': TextInput(),
            'transaction_date':TextInput(),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'