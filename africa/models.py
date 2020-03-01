from django.db import models

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
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name