from django.db import models

# Create your models here.

class Menu(models.Model):

	products = ""
	category = ""
	restaurant = ""


class Product(models.Model):

	name = ""
	price = 0.0
	ingredients = ""
	category = ""

	def evaluateProduct(diner):
		return diner

	def discardProduct(diner):
		return True

