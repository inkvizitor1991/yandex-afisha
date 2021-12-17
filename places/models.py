from django.db import models
from tinymce.models import HTMLField


class Places(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Короткое описание', blank=True)
    description_long = HTMLField('Полное описание', blank=True)
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'


class Images(models.Model):
    places = models.ForeignKey(
        Places, on_delete=models.CASCADE,
        related_name='images'
    )
    order = models.PositiveIntegerField('Номер')
    image = models.ImageField('Картинка')

    def __str__(self):
        return f'{self.order} {self.places.title}'

    class Meta:
        ordering = ['order']
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
