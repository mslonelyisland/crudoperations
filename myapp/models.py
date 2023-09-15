from django.db import models

# Create your models here.
class Orders(models.Model):  
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    status = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100) 
    notes = models.CharField(max_length=100)
    figures = models.IntegerField(max_length=20)
    payment = models.CharField(max_length=100, default='Not specified')
    paid = models.CharField(max_length=100, default='Not specified')

   
    class Meta:  
        db_table = "tborder"
