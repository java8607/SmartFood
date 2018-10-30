from django.db import models

# Create your models here.

class Schedule():

	manager = None
	menu = None
	days = ""

	def __init__(self, manager, menu):
		self.manager = Manager()
		self.menu = Menu()







