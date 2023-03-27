from django.db import models

# Create your models here.
class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(default=None)
    phonenumber = models.IntegerField(default='+234-80283884892')
    serialNumber = models.IntegerField(default='serial_123456')
    location = models.TextField(default='no location')


