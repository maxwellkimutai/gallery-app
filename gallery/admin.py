from django.contrib import admin
from .models import Location, categories, Image

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories',)

admin.site.register(Location)
admin.site.register(Image,ImageAdmin)
admin.site.register(categories)
