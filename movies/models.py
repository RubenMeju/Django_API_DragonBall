from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=275)
    air_date = models.DateField()
    image = models.ImageField(upload_to='movies')

    def __str__(self):
        return self.name
