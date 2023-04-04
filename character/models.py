from django.db import models
from planet.models import Planet


class Character(models.Model):
  
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='characters')
    planet = models.ForeignKey(
        Planet, on_delete=models.CASCADE, related_name='planet')

    def __str__(self):
        return self.name
