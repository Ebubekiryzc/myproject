from django.db import models

# Create your models here.
# Burada models.Model bu basit sınıfı gerçek bir veri tabanı nesnesine dönüştürmektedir.


class Feature(models.Model):
    # id: int
    # eskiden str idi ve name iki nokta str idi :
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    # is_true: bool
