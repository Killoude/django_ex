from django.contrib import admin
from .models import Customers, Products, Transaction, Detail_transaction, Users
# Register your models here.

#class ChoiceInLine(admin.TabularInline):
    #model = Choice
    #extra = 3


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('nota', 'transanction_date')
    #list_filter = ['pub_date']
    #search_fields = ['question_text']
    
    fieldsets = [
        (None,               {'fields': ['nota']}),
        ('Date information', {'fields': ['transanction_date'], 'classes': ['collapse']}),
    ]
    #inlines = [ChoiceInLine]

class ProductAdmin(admin.ModelAdmin):
    list_display =('code', 'detail', 'type_product', 'packing', 'crt', 'pcs')
    list_filter = ['type_product']
    search_fields = ['code']
    fieldsets = [
        ('Products Information',               {'fields': ['code', 'detail', 'type_product', 'packing', 'crt', 'pcs']}),
    ]

admin.site.register(Transaction)
admin.site.register(Products, ProductAdmin)

