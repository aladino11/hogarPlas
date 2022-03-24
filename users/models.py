from multiprocessing import Condition
from django.db import models
from django.forms import PasswordInput

# Create your models here.
class Rol(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    Condition = models.BooleanField(max_length=50)


class Users(models.Model):
    first_names= models.CharField(max_length=255)
    last_names= models.CharField(max_length=255)
    type_id= models.CharField(max_length=125)
    num_document= models.CharField(max_length=50)
    address= models.CharField(max_length=300)
    phone= models.CharField(max_length=20)
    email= models.CharField(max_length=300)
    Password= models.CharField(max_length=10)
    Condition= models.CharField(max_length=50)
    rol= models.ForeignKey(Rol,on_delete=models.CASCADE)

class category(models.Model):
    id_category= models.CharField(max_length=255)
    name= models.CharField(max_length=250)
    description= models.CharField(max_length=500)
    Condition= models.BooleanField(max_length=50)