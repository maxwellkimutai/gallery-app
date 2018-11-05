from django.test import TestCase
from .models import Image, Location, categories

# Create your tests here.
class LocationTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.location = Location(id = 1,name = 'Nairobi')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

    #Testing Save method
    def test_save_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_update_method(self):
        self.location.save_location()
        self.location = Location.objects.filter(name = 'Nairobi').update(name = 'Nakuru')
        self.updated_location = Location.objects.get(name = 'Nakuru')
        self.assertEqual(self.updated_location.name,"Nakuru")

    def test_delete_method(self):
        self.location.save_location()
        self.location = Location.objects.get(id = 1)
        self.location.delete_location()
        self.assertTrue(len(Location.objects.all()) == 0)

class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.location = Location(name = "Nairobi")
        self.location.save_location()
        self.image = Image(id = 1,title = "test",description = "test description",location = self.location, image_url = "path/to/image")

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    def test_save_image(self):
        self.image.save_image()
        self.images = Image.objects.all()
        self.assertTrue(len(self.images) > 0)

    def test_get_image_by_id(self):
        self.image.save_image()
        self.image = Image.get_image_by_id(1)
        self.assertTrue(isinstance(self.image,Image))

    def test_update_image(self):
        self.image.save_image()
        self.image = Image.objects.filter(id = 1).update(image_url = "new/path/to/image")
        self.updated_image = Image.get_image_by_id(1)
        self.assertEqual(self.updated_image.image_url,"new/path/to/image")

    def test_search_by_category(self):
        self.image.save_image()
        self.category = categories(name = "test")
        self.category.save_category()
        self.image = Image.get_image_by_id(1).categories.add(self.category)
        self.searched_images = Image.search_by_category('test')
        self.assertTrue(len(self.searched_images) > 0)

    def test_filter_by_location(self):
        self.image.save_image()
        self.searched_images = Image.filter_by_location('Nairobi')
        self.assertTrue(len(self.searched_images) > 0)

    def test_delete_image(self):
        self.image.save_image()
        self.searched_image = Image.get_image_by_id(1)
        self.searched_image.delete_image()
        self.assertTrue(len(Image.objects.all()) == 0)

class CategoriesTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.category = categories(id = 1,name = 'test')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.category,categories))

    #Testing Save method
    def test_save_method(self):
        self.category.save_category()
        self.categories = categories.objects.all()
        self.assertTrue(len(self.categories) > 0)

    def test_update_method(self):
        self.category.save_category()
        self.category = categories.objects.filter(name = 'test').update(name = 'changed')
        self.updated_category = categories.objects.get(name = 'changed')
        self.assertEqual(self.updated_category.name,"changed")

    def test_delete_method(self):
        self.category.save_category()
        self.category = categories.objects.get(id = 1)
        self.category.delete_category()
        self.assertTrue(len(categories.objects.all()) == 0)
