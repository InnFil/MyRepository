from django.db import models


class Section(models.Model):
    name = models.TextField(verbose_name='Название', max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cекция'
        verbose_name_plural = 'Секции'
