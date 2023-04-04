from django.db import models
from season.models import Season


class Chapter(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=50)
    summary = models.TextField()
    #image = models.ImageField(upload_to='media/chapters')
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
