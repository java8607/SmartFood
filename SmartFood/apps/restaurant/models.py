from django.db import models

from apps.user.models import User

# Create your models here.
class Ingredient(models.Model):
	name = models.CharField(max_length=50)
	category = models.CharField(max_length=50)
	amount = models.IntegerField()
		
class Product(models.Model):
	name = models.CharField(max_length=50)
	price = models.FloatField()
	ingredient = models.ManyToManyField(Ingredient)
	
class Menu(models.Model):
	product = models.ManyToManyField(Product)
	category = models.CharField(max_length=50)
	
class Restaurant(models.Model):
	menu = models.OneToOneField(Menu, null=True, blank=True, on_delete=models.CASCADE)
	address = models.TextField()	
	phoneNumber = models.CharField(max_length=12)
	phoneNumberAlternative = models.CharField(max_length=12)
	cellPhoneNumber = models.CharField(max_length=12)
	cellPhoneNumberAlternative = models.CharField(max_length=12)
	coordinates = models.TextField()

class Schedule(models.Model):
	day = models.CharField(max_length=9)
	openningTime = models.TimeField()
	clousingTime = models.TimeField()
	restaurant = models.ForeignKey(Restaurant, null=True, blank=True, on_delete=models.CASCADE)

class Manager(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	restaurant = models.OneToOneField(Restaurant, null=True, blank=True, on_delete=models.CASCADE)
	