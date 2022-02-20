from django.db import models


# Create your models here.
class Coin(models.Model):
    coin_name = models.CharField(max_length=200)
    country = models.CharField(max_length=30)
    release_year = models.IntegerField(default=1970)
    amount = models.IntegerField(default=0)
    currency = models.CharField(max_length=10)
    time_obtained = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    time_added = models.IntegerField(default=0)
    description = models.CharField(max_length=500)
