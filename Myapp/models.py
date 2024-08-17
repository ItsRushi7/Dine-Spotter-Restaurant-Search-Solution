from django.db import models

# Create your models here.

class USERPASS(models.Model):
    
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Signup(models.Model):
    
    Name = models.CharField(max_length=100)
    Phone_Number = models.CharField(max_length=100)
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    
class Resturant(models.Model):
    
    RestaurentId = models.CharField(max_length=100)
    RestaurentName = models.CharField(max_length=100)
    RestaurentEmail = models.CharField(max_length=100)
    RestaurentAddress = models.CharField(max_length=100)
    RestaurentPhone = models.CharField(max_length=100)
    RestaurentServices = models.CharField(max_length=100)