from django.db import models
# Create your models here.

class Artist(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	instrument = models.CharField(max_length=80,blank=True, null=True)
	musical_gender = models.CharField(max_length=90, null=True)

	
	def __str__(self):
		return self.name
