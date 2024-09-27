from django.db import models

from artist.models import Artist

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=255)
    released_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to="album_cover_pages/", blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.artist}"