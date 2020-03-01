from django.test import TestCase
from .models import Location, Category, Image

class TestLocation(TestCase):
    '''Test class to test location class'''
    def setUp(self):
        '''Function to prepare for every test case'''
        self.test_location = Location(location = 'Nairobi')

    def tearDown(self):
        '''Function to clean up after every test case'''
        Location.objects.all().delete()

    def test_isinstance(self):
        '''Test if test_location is an instance of location class'''
        self.assertTrue(isinstance(self.test_location, Location))

    def test_save_location(self):
        '''Test saving a location to database'''
        self.test_location.save_class()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_location(self):
        '''Test deleting a location'''
        self.test_location.save_class()
        self.test_location.delete_class()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)

    def test_update_location(self):
        '''Test case to update a location in database'''
        self.test_location.save_class()
        self.test_location.update_class(location = 'Kisumu')
        self.assertEqual(self.test_location.location, 'Kisumu')

class TestCategory(TestCase):
    '''Test class to test category class'''
    def setUp(self):
        '''Function to prepare for every test case'''
        self.test_category = Category(category = 'landscape')

    def tearDown(self):
        '''Function to clean up after every test case'''
        Category.objects.all().delete()

    def test_isinstance(self):
        '''Test if test_category is an instance of category class'''
        self.assertTrue(isinstance(self.test_category, Category))

    def test_save_category(self):
        '''Test saving a category to database'''
        self.test_category.save_class()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        '''Test deleting a category'''
        self.test_category.save_class()
        self.test_category.delete_class()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)

    def test_update_category(self):
        '''Test case to update a category in database'''
        self.test_category.save_class()
        self.test_category.update_class(category = 'adventure')
        self.assertEqual(self.test_category.category, 'adventure')


class TestImage(TestCase):
    '''Test class to test Image class'''
    def setUp(self):
        '''Function to prepare for every test case'''
        # Category
        self.test_category = Category(category = 'landscape')
        self.test_category.save_class()
        # Location
        self.test_location = Location(location = 'Nairobi')
        self.test_location.save_class()
        # Image
        self.test_image = Image(image_name='Somalia', image_description='The beautiful land in the east', category=self.test_category, location=self.test_location)

    def tearDown(self):
        '''Function to clean up after every test case'''
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    def test_isinstance(self):
        '''Test if test_image is an instance of image class'''
        self.assertTrue(isinstance(self.test_image, Image))

    def test_save_image(self):
        '''Test saving a image to database'''
        self.test_image.save_class()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        '''Test deleting a image'''
        self.test_image.save_class()
        self.test_image.delete_class()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_image(self):
        '''Test case to update and object in database'''
        self.test_image.save_class()
        self.test_image.update_class(image_name = 'Which Mogadishu')
        self.assertEqual(self.test_image.image_name, 'Which Mogadishu')
