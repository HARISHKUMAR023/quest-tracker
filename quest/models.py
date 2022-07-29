from django.db import models


# Create your models here.
class ceo(models.Model):
      
    email=models.EmailField()
    password=models.CharField(max_length=120)
class manager(models.Model):
      
    email=models.EmailField()
    password=models.CharField(max_length=120)    
