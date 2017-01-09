from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	title = models.CharField(max_length = 90)
	text = models.TextField()

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title