from django.db import models


class Places(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Короткое описание', blank=True)
    description_long = models.TextField('Полное описание', blank=True)
    lat = models.FloatField(verbose_name='Широта', blank=True, null=True)
    lon = models.FloatField(verbose_name='Долгота', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'


class Images(models.Model):
    places = models.ForeignKey(
        Places, on_delete=models.CASCADE,
        related_name='images',
        blank=True, null=True
    )
    order = models.PositiveIntegerField('Номер', blank=True, null=True)
    image = models.ImageField(
        'Картинка',
        blank=True, null=True
    )

    def __str__(self):
        return f'{self.order} {self.places.title}'

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
