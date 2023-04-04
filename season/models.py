from django.db import models
from episode.models import Episode

class Season(models.Model):
    title = models.CharField(max_length=50)
    number_chapters = models.IntegerField(null=True)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
