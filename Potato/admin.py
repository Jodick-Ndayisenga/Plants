from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Picture)
admin.site.register(Picinfo)
admin.site.register(AllPlants)
admin.site.register(PlantInformation)


admin.site.site_header = "AgriTech Pioneers"
admin.site.site_title = "Le gardien éveillé"
admin.site.index_title = "AgriTech Pioneers dashboard"
