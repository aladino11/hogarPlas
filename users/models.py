from multiprocessing import Condition
from tkinter import Entry
from django.db import models
from django.forms import PasswordInput

# Create your models here.
class Rol(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    Condition = models.BooleanField()


class Users(models.Model):
    first_names= models.CharField(max_length=255)
    last_names= models.CharField(max_length=255)
    type_id= models.CharField(max_length=125)
    num_document= models.IntegerField()
    address= models.CharField(max_length=300)
    phone= models.CharField(max_length=20)
    email= models.CharField(max_length=300)
    Password= models.CharField(max_length=10)
    Condition= models.BooleanField()
    rol= models.ForeignKey(Rol,on_delete=models.CASCADE)

class category(models.Model):
    id_category= models.CharField(max_length=255)
    name= models.CharField(max_length=250)
    description= models.CharField(max_length=500)
    Condition= models.BooleanField()

class Sale_detail(models.Model):
    amount= models.IntegerField()
    price= models.DecimalField(max_digits=11, decimal_places=2)
    descuento= models.DecimalField(max_digits=11, decimal_places=2)
    sale= models.ForeignKey(Sale, on_delete=models.RESTRICT)
    article= models.ForeignKey(article, on_delete=models.RESTRICT)

class Sale(models.Model):
    type_voucher= models.CharField(max_length=200)
    serial_voucher= models.CharField(max_length=300)
    mun_voucher= models.IntegerField()
    date_hour= models.DateTimeField(auto_now=False, auto_now_add=False)
    tax= models.DecimalField(max_digits=4, decimal_places=2)
    total= models.DecimalField(max_digits=11, decimal_places=2)
    state= models.CharField(max_length=100)
    Person= models.ForeignKey(Person, on_delete=models.RESTRICT)
    users= models.ForeignKey(Users, on_delete= models.RESTRICT)

class Income_detail(models.Model):
    amont= models.IntegerField()
    entry= models.ForeignKey(Entry, on_delete= models.RESTRICT)
    article= models.ForeignKey(article, on_delete= models.RESTRICT)


    