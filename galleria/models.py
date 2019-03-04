from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length = 30)

class Category(models.Model):
    name = models.CharField(max_length = 30)

class Image(models.Model):
    image_url = models.ImageField(upload_to = "images/")
    name = models.CharField(max_length = 30)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)