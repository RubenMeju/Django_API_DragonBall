from django.db import models
from season.models import Season


class Episode(models.Model):
    title = models.CharField(max_length=50)
    synopsis = models.TextField()
    air_date = models.DateField()
    image = models.ImageField(upload_to='media/episodes')
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
