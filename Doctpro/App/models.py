from django.db import models

# Create your models here.
class Registration(models.Model):
	#id = models.AutoField;	
	Mobile =  models.IntegerField(default=0)
	

class Login(models.Model):
	Mobile = models.IntegerField(default=0)
	#Mobile =  models.IntegerField(default=0)
	