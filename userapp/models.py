from django.db import models

# Create your models here.
class userdb(models.Model):
    abc=models.ImageField(upload_to='media',null=True,blank=False)
    lname=models.CharField(max_length=100,null=True,blank=False)
    fname=models.CharField(max_length=100,null=True,blank=False)
    password=models.CharField(max_length=100,null=True,blank=False)
    number=models.IntegerField(null=True,blank=False)
    email=models.CharField(max_length=100,null=True,blank=False)