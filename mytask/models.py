from django.db import models
from django.urls import reverse

# Create your models here.
class contact(models.Model):
	name = models.CharField(max_length=30)
	contactno = models.BigIntegerField()
	district = models.TextField()

	def get_absolute_url(self):
		return reverse('showsubcriber')

	def __str__(self):
		return self.name