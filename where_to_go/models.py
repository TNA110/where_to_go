from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = HTMLField()
    longtitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.title

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(blank = True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, blank=False, editable=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False, editable=True)
   
    class Meta(object):
        ordering = ['my_order',]

    def __str__(self):
        return self.title
        
