from django.db import models

# Create your models here.
class Product(models.Model):
    Name_of_product=models.CharField(max_length=50)
    Provider = models.CharField(max_length=50)
    Date=models.DateField()
    Price = models.FloatField()
    Quantity = models.IntegerField()
    Amount = models.FloatField()
    Stock = models.IntegerField()
