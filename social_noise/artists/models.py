from django.db import models
# Create your models here.

class Artist(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()

class Musician(models.Model):
	instrument = models.CharField(max_length=60)
	musical_gender = models.CharField(max_length=50, blank=True, null=True)


	def __str__(self):
		return self.name
