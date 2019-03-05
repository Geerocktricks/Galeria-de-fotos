from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Image(models.Model):
    image_url = models.ImageField(upload_to = "today/")
    name = models.CharField(max_length = 30)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.name


    @classmethod
    def get_image_by_id(cls,image_id):
        """
        This is the method to get a specific image
        """
        return cls.objects.get(id = image_id)

    @classmethod
    def get_images(cls):
        return cls.objects.all()

    @classmethod
    def search_image(cls,category):
        """
        This is the method to search images based on a specific category
        """
        print('Text')
        try:   
            searched_category = Image.objects.filter(category__name__icontains  = category)
            return searched_category
        except Exception:
            return "No images found"
    @classmethod
    def filter_by_location(cls,location):
        """
        This is the method to get images taken in a certain location
        """
        the_location = Location.objects.get(name = location)
        return cls.objects.filter(location_id = the_location.id)

    def __str__(self):
        return self.name