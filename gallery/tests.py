from django.test import TestCase
from .models import Image, Location, categories

# Create your tests here.
class LocationTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.nairobi = Location(name = 'Nairobi')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))

    #Testing Save method
    def test_save_method(self):
        self.james.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)
