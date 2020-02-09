from django.db import models

# Create your models here.

class sbu(models.Model):
	provinsi	= models.CharField(max_length=100)
	uang_harian	= models.IntegerField()

	def __str__(self):
		return "{}. {}".format(self.id, self.provinsi)