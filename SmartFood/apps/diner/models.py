from django.db import models

from apps.user.models import User
from apps.restaurant.models import Ingredient


# Create your models here.
class Diner(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	budget = models.FloatField()
	religion = models.CharField(max_length=50)
	nacionality = models.CharField(max_length=50)
	region = models.CharField(max_length=50)
	weightKg = models.FloatField()	

class HealthCharacteristic(models.Model):
	name = models.CharField(max_length=50)
	category = models.CharField(max_length=50)
	ingredient = models.ManyToManyField(Ingredient)
	user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

class Preference(models.Model):
	favouriteTypeOfProduct = models.CharField(max_length=50)
	isGlutton = models.BooleanField()
	ingredient = models.ManyToManyField(Ingredient)
	user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)