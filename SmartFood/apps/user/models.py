from django.db import models

# Create your models here.
class User(models.Model):
	userName = models.CharField(max_length=50)
	firstName = models.CharField(max_length=50)
	lastName = models.CharField(max_length=50)
	password = models.CharField(max_length=12)
	address = models.TextField()
	birthDate = models.DateField(null=True, blank=True)
	phoneNumber = models.CharField(max_length=12)
	cellPhoneNumber = models.CharField(max_length=12)