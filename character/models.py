from django.db import models
from planet.models import Planet


class Character(models.Model):
    # sexo
    FEMALE = 'FE'
    MALE = 'MA'
    GENDER_CHOICES = [
        (FEMALE, 'Woman'),
        (MALE, 'Men'),
    ]
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    gender = models.CharField(
        max_length=2, choices=GENDER_CHOICES, blank=False)

    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='characters')
    abilities = models.CharField(max_length=200)
    planet = models.ForeignKey(
        Planet, on_delete=models.CASCADE, related_name='planet')

    def __str__(self):
        return self.name
