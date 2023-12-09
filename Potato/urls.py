from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Potato'
urlpatterns = [
    path("", views.index, name="index"),
    path("predict", views.predict, name="predict"),
    path("agribot",views.agribot, name="agribot"),
    path("crop-recommender", views.crop_recommendation, name= "crop"),
    path("fertilizer-recommender", views.fertilizer_recommendation, name= "fertilizer"),
    path('<int:plant_id>', views.myPlantInformation, name='plantInformation')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)