from django.db import models
from django.core.validators import MaxValueValidator


class Floor(models.Model):
    DIODE = 'DIODE'
    LUMINESCENT = 'LUMINESCENT'

    CHOICES = (
        (DIODE, 'Диодное'),
        (LUMINESCENT, 'Люминесцентное'),
    )

    number = models.IntegerField(verbose_name='Номер', validators=[MaxValueValidator(25)])
    color = models.TextField(verbose_name='Цвет', validators=[MaxValueValidator(225)])
    lighting = models.TextField(verbose_name='Освещение', validators=[MaxValueValidator(225)], choices=CHOICES)

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = 'Этаж'
        verbose_name_plural = 'Этажи'
