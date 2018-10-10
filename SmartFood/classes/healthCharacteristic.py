from django.db import models

# Create your models here.

class HealthCharacteristic():

	restaurant = None
	isDiabetic = False
	hasHealthDesease = False
	allergicProfile = ()

	def __init__(self, restaurant):
		self.manager = Manager()
		self.menu = Menu()

	def getAllergicProfile(self, allergicProfile):
		return allergicProfile







