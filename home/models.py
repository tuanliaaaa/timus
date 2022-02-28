import email
from operator import mod
from django.db import models
from django.forms import EmailField

# Create your models here.
class Product(models.Model):
    ProductName = models.CharField(max_length=100)
    ProductCode = models.CharField(max_length=10)
    price = models.IntegerField()
    stock = models.IntegerField()
    describe = models.CharField(max_length=500)
    img = models.CharField(max_length=10000)
    sale = models.IntegerField(default=0)
class Users(models.Model):
    UserName = models.CharField(max_length=100)
    Number = models.CharField(max_length=12)
    email = models.EmailField()
    Sex = models.CharField(max_length=4)
class Buy(models.Model):
    Users = models.ForeignKey(Users,on_delete=models.CASCADE)
    Product =models.ForeignKey(Product,on_delete= models.CASCADE)
    quantily = models.IntegerField()
    BuyTime = models.DateTimeField(auto_now_add=True)
