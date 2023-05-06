from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(name='item_name', max_length=255)
    disk = models.CharField(name='item_disc', max_length=255)
    price = models.CharField(name='item_price', max_length=255)
    img = models.CharField(name='img', max_length=255)

