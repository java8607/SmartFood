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
	
	def getBudget(self):
		return self.budget
	
	def getPreferences(self):
		return self.preferences
	
	def setBudget(self, budget):
		self.budget = budget
		
	def setPreferences(self, preferences):
		self.preferences = preferences
		






