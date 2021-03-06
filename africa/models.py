from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import cloudinary

class CrudMethods:
    '''Method class for Common methods'''
    def save_class(self):
        '''Function to save class to database'''
        self.save()

    def delete_class(self):
        '''Function to delete class from database'''
        self.delete()

    def update_class(self, **kwargs):
        '''Function to update the class in database'''
        for key,value in kwargs.items():
            setattr(self,key,value)
            self.save()

class Location(models.Model, CrudMethods):
    '''Location model for the image location details'''
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location

class Category(models.Model, CrudMethods):
    '''Category Model containing the image category details'''
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

class Image(models.Model, CrudMethods):
    '''Image Class containing the Image details'''
    image_name = models.CharField(max_length=30)
    image_description = models.TextField()
    image = CloudinaryField('image') 
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    @classmethod
    def get_images(cls):
        '''Class method to get all the images stored in database'''
        images = Image.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls, image_id):
        '''Class method to get a specific image by it's id'''
        image = cls.objects.filter(id = image_id).first()
        return image

    @classmethod
    def search_images(cls, search_category):
        '''Class method to search for images'''
        images = cls.objects.filter(category__category = search_category)
        return images

    @classmethod
    def filter_by_location(cls, search_location):
        '''Class method to filter images by location'''
        images = cls.objects.filter(location__location = search_location)
        return images
        
    def __str__(self):
        return self.image_name

@receiver(pre_delete, sender=Image)
def photo_delete(sender, instance, **kwargs):
    '''Cloudinary's Predelete signal to tell cloudinary to delete image when model is deleted'''
    cloudinary.uploader.destroy(instance.image.public_id)