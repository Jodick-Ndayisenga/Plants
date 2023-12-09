from django.db import models

# Create your models here.
class Picture(models.Model):
    # Values from the JSON file
    TITLE_CHOICES = [
        ("10-26-26"),
        ("14-35-14"),
        ("17-17-17"),
        ("20-20"),
        ("28-28"),
        ("DAP"),
        ("Urea"),
    ]

    title = models.CharField(max_length=10, choices=[(value, value) for value in TITLE_CHOICES], blank=False)
    preview = models.ImageField(upload_to='static/images', null=False, blank=False)
    comments = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title}'


class Picinfo(models.Model):
    item = models.ForeignKey(
        Picture, on_delete=models.CASCADE, blank=False, null=False)
    description_sizes = models.TextField(
        blank=False, name='des_sizes', max_length=360)
    captured_time = models.DateField(blank=False)
    price = models.IntegerField(blank=False)

    def __str__(self):
        return f'{self.item}'


class AllPlants(models.Model):
    choices = [
    ("apple"),
    ("pear"),
    ("cherry"),
    ("banana"),
    ("plantain"),
    ("papaya"),
    ("blackgram"),
    ("green gram"),
    ("lentil"),
    ("chickpea"),
    ("fava bean"),
    ("soybean"),
    ("coconut"),
    ("oil palm"),
    ("betel nut"),
    ("coffee"),
    ("cocoa"),
    ("tea"),
    ("cotton"),
    ("flax"),
    ("hemp"),
    ("grapes"),
    ("wineberries"),
    ("kiwi"),
    ("jute"),
    ("sisal"),
    ("flax"),
    ("kidneybeans"),
    ("navy beans"),
    ("lima beans"),
    ("lentil"),
    ("chickpea"),
    ("blackgram"),
    ("maize"),
    ("wheat"),
    ("barley"),
    ("mango"),
    ("guava"),
    ("papaya"),
    ("mothbeans"),
    ("blackgram"),
    ("green gram"),
    ("mungbean"),
    ("blackgram"),
    ("mothbeans"),
    ("muskmelon"),
    ("cucumber"),
    ("pumpkin"),
    ("orange"),
    ("lemon"),
    ("lime"),
    ("papaya"),
    ("mango"),
    ("guava"),
    ("pigeonpeas"),
    ("lentil"),
    ("chickpea"),
    ("pomegranate"),
    ("fig"),
    ("quince"),
    ("rice"),
    ("barley"),
    ("wheat"),
    ("watermelon"),
    ("cantaloupe"),
    ("cucumber")
]

    title = models.CharField(max_length=1000, choices=[(value, value) for value in choices], blank=False)
    preview = models.ImageField(upload_to='static/images', null=False, blank=False)
    comments = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title}'

class PlantInformation(models.Model):
    item = models.ForeignKey(
        AllPlants, on_delete=models.CASCADE, blank=False, null=False)
    description_sizes = models.TextField(
        blank=False, name='des_sizes', max_length=500)
    captured_time = models.DateField(blank=False)
    price = models.IntegerField(blank=False)

    def __str__(self):
        return f'{self.item}'