from django.db import models

class Image(models.Model):
    url = models.CharField(max_length=255)
    dice = models.ForeignKey('Dice', on_delete=models.CASCADE)

class Dice(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sold = models.BooleanField()