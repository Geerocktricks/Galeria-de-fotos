from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

# class Image(models.Model):
#     image_url = models.ImageField(upload_to = "images/")
#     name = models.CharField(max_length = 30)
#     description = models.TextField()
#     location = models.ForeignKey(Location)
#     category = models.ForeignKey(Category)
    #   pub_date = models.DateTimeField(auto_now_add=True)

    #    def __str__(self):
    #            return self.name