from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Picture)
admin.site.register(Picinfo)
admin.site.register(AllPlants)
admin.site.register(PlantInformation)
