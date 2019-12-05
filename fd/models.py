import datetime

from django.db import models
from django.utils import timezone

class Users(models.Model):
    username = models.CharField(max_length=11)
    password = models.CharField(max_length=11)
    role_type = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(default=0)

    def __str__(self):
        return self.username


    def delete(self):
        self.deleted_at = timezone.now()
        #self.deleted_by = this user
        self.deleted = 1
        self.save


class Customers(models.Model):
    name = models.TextField()
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=11,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    #userid
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(default=0)

    def __str__(self):
        return self.name


    def delete(self):
        self.deleted_at = timezone.now()
        #self.deleted_by = this user
        self.deleted = 1
        self.save


class Products(models.Model):
    code = models.CharField(max_length=11)
    detail = models.TextField()
    type_product = models.CharField(blank=True, null=True, max_length=11)
    packing = models.CharField(blank=True, null=True, max_length=11)
    crt = models.IntegerField()
    pcs = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    #userid
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(default=0)

    # def __str__(self):
    #     return self.code
    def delete(self):
        self.deleted_at = timezone.now()
        #self.deleted_by = this user
        self.deleted = 1
        self.save


# Create your models here.
class Transaction(models.Model):
    nota = models.CharField(max_length = 11, null = True)
    customers = models.ForeignKey(Customers, on_delete = models.CASCADE)
    customers_name = models.CharField(max_length= 255)
    transaction_date = models.DateField()
    status = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    #userid
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(default=0)
    # objects = SoftDeletionManager()
    # all_objects = SoftDeletionManager(alive_only=False)
    
    def __str__(self):
        return self.nota


    def delete(self):
        self.deleted_at = timezone.now()
        #self.deleted_by = this user
        self.deleted = 1
        self.save


class Detail_transaction(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete = models.CASCADE)
    product = models.ForeignKey(Products, on_delete = models.CASCADE)
    crt = models.IntegerField()
    pcs = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    #userid
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(default=0)

    def __str__(self):
        return self.product


    def delete(self):
        self.deleted_at = timezone.now()
        #self.deleted_by = this user
        self.deleted = 1
        self.save


