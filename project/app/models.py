from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True, default=None, blank=True)
    price = models.FloatField()