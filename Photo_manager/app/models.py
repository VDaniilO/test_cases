from django.db import models


class PhotoModel(models.Model):
    photo = models.ImageField(upload_to='photo/')
    geo_locate = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    people_on_photo = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.photo.url