from django.db import models

# Create your models here.
class Products(models.Model):
    Name_of_Product=models.CharField(max_length=50)
    Provider=models.CharField(max_length=50)
    Date=models.DateField()
    Price=models.FloatField()
    Quantity=models.IntegerField()
    Amount=models.FloatField()
    Stock=models.IntegerField()
