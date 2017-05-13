from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    title=models.CharField(max_length=5)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=300)
    password=models.CharField(max_length=40)
    repassword=models.CharField(max_length=40)
    mobile=models.CharField(max_length=10)
    def __str__(self):
       return self.first_name+"-"+self.last_name

class Store(models.Model):
    store_name=models.CharField(max_length=200)
    rating=models.CharField(max_length=2)
    review=models.CharField(max_length=200)
    date=models.DateField(max_length=25)
    totalproduct=models.CharField(max_length=10)
    def __str__(self):
        return self.store_name