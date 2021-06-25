from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description_short = models.TextField(verbose_name="Краткое описание")
    description_long = HTMLField(verbose_name="Полное описание")
    longtitude = models.FloatField(verbose_name="Долгота")
    latitude = models.FloatField(verbose_name="Широта")

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    image = models.ImageField(blank=True, verbose_name="Изображение")
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name="Локация")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядковый номер")

    class Meta(object):
        ordering = ['order', ]

    def __str__(self):
        return self.title
