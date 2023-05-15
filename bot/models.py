from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=50)
    rating = models.CharField(max_length=10)