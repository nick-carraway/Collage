from django.db import models

# Create your models here.

class Photo(models.Model):
	image = models.ImageField(upload_to = 'images/', default = 'images/None/no-img.jpg')

# TODO: add Comments and PhotoMetadata models
