from django.db import models

# Create your models here.

class Diner():

	budget = 0.0
	preferences = ()
	personalCharacteristic = ()
	healthCharacteristic = ()

	def __init__(self, personalCharacteristic, healthCharacteristic):
		self.healthCharacteristic = healthCharacteristic
		self.personalCharacteristic = personalCharacteristic







