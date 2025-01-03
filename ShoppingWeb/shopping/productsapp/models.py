from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock = models.IntegerField()
    isTreanding = models.BooleanField(default=False)
    image = models.ImageField(upload_to='products', blank=True)