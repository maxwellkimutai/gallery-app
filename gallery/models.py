from django.db import models

# Create your models here.
class categories(models.Model):
    name = models.CharField(max_length=30)

    def save_category(self):
        self.save()

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=30)

    def save_location(self):
        self.save()

    def __str__(self):
        return self.name
