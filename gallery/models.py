from django.db import models

# Create your models here.
class categories(models.Model):
    name = models.CharField(max_length=30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name

class Image(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    categories = models.ManyToManyField(categories)
    image_url = models.ImageField(upload_to = 'images/',blank=True)

    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(categories__name__contains = search_term)
        if len(images) < 1:
            case_images = cls.objects.filter(categories__name__contains = search_term.capitalize())
            return case_images
        else:
            return images
    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.get(id = id)
        return image

    @classmethod
    def filter_by_location(cls,search_term):
        location = Location.objects.get(name = search_term)
        images = cls.objects.filter(location = location)
        return images
