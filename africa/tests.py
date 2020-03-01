from django.test import TestCase
from .models import Location, Category, Image

class TestLocation(TestCase):
    '''Test class to test location class'''
    def setUp(self):
        '''Function to prepare for every test case'''
        self.test_location = Location('Nairobi')

    def tearDown(self):
        '''Function to clean up after every test case'''
        Location.objects.all().delete()
