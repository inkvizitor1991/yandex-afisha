from django.db import models


class Places(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'



