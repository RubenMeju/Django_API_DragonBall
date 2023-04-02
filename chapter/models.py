from django.db import models
from episode.models import Episode


class Chapter(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=50)
    summary = models.TextField()
    image = models.ImageField(upload_to='media/chapters')
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
