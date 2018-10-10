from django.db import models

# Create your models here.

class Restaurant():

	manager = None
	menu =  None
	address = ""
	coordinates = ""
	phoneNumber = ""
	phoneAlternative = ""
	cellPhoneNumber = ""
	CellPhoneNumberAlternative = ""

	def __init__(self, manager, menu):
		manager = Manager()
		menu = Menu()
		
	def getManager(self):
		return self.manager
	
	def getMenu(self):
		return self.menu
	
	def getAddress(self):
		return self.address

	
