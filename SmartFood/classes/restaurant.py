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

	def __init__(manager, menu):
		manager = Manager(self)
		menu = Menu()

	