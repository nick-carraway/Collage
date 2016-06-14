from django.db import models

# Create your models here.

class Photo(models.Model):
	title = models.CharField(max_length=32)
	image = models.ImageField(upload_to = 'images/', default = 'images/None/no-img.jpg')

# TODO: add Comments and PhotoMetadata models
