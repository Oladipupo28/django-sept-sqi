from django.db import models

from artist.models import Artist

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=255)
    released_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title