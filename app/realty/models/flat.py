from django.db import models
from django.core.validators import MaxValueValidator


class Flat(models.Model):
    ON_SALE = 'ON_SALE'
    SOLD = 'SOLD'

    CHOICES = (
        (ON_SALE, 'Доступно к покупке'),
        (SOLD, 'Продано'),
    )

    description = models.TextField(verbose_name='Описание', blank=True, max_length=255)
    photo = models.ImageField(verbose_name='Фото', upload_to="photos/%Y/%m/%d/")
    price = models.IntegerField(verbose_name='Цена')
    square = models.IntegerField(verbose_name='Площадь', validators=[MaxValueValidator(1000)])
    rooms = models.IntegerField(verbose_name='Количество комнат', validators=[MaxValueValidator(50)])
    number = models.IntegerField(verbose_name='Номер', validators=[MaxValueValidator(1000)])
    status = models.TextField(verbose_name='Статус', max_length=255, choices=CHOICES)
    floor = models.ForeignKey('Floor', on_delete=models.PROTECT, verbose_name='Этаж')
    section = models.ForeignKey('Section', on_delete=models.PROTECT, null=True, verbose_name='Секция')
    building = models.ForeignKey('Building', on_delete=models.PROTECT, null=True, verbose_name='Корпус')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'
