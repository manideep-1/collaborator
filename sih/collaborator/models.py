from django.db import models

# Create your models here.

class destination(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField(max_length=200)
    mobile=models.CharField(max_length=12)
    password= models.CharField(max_length=32)
    upload = models.FileField(upload_to='upload/',null=True,blank=True)
    notification = models.CharField(max_length=100,blank=True)
    skills=models.CharField(max_length=1000,blank=True)

class destinationclient(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField(max_length=200)
    mobile=models.CharField(max_length=12)
    password= models.CharField(max_length=32)
    nametodisplay=models.CharField(max_length=100,blank=True)
    req=models.CharField(blank=True,max_length=10000)
    notification = models.CharField(max_length=100,blank=True)

class destinationcompany(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField(max_length=200)
    mobile=models.CharField(max_length=12)
    password= models.CharField(max_length=32)
    organizationname=models.CharField(max_length=100,blank=True)
    

