from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=40, blank=False, unique=True)
	description = models.TextField(max_length=500, blank=True)
	price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
	published = models.DateField(default=None)
	is_published = models.BooleanField(default=None)
	cover = models.ImageField(upload_to = "covers/", default=None)

	def __str__(self):
		return self.title
