from django.db import models


class Season(models.Model):
    title = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title