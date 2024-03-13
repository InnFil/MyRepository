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
    floor = models.ForeignKey('Floor', on_delete=models.PROTECT)
    section = models.ForeignKey('Section', on_delete=models.PROTECT, null=True)
    building = models.ForeignKey('Building', on_delete=models.PROTECT, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'


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


class Section(models.Model):
    name = models.TextField(verbose_name='Название', max_length=255, unique=True)


class Building(models.Model):
    COMPLETE = 'COMPLETE'
    CONSTRUCTION = 'CONSTRUCTION'
    BRICK = 'BRICK'
    PANEL = 'PANEL'
    MONOLITHIC = 'MONOLITHIC'

    STATUS_CHOICES = (
        (COMPLETE, 'Сдан'),
        (CONSTRUCTION, 'Строится'),
    )
    HOUSE_TYPE_CHOICES = (
        (BRICK, 'Кирпичный'),
        (PANEL, 'Панельный'),
        (MONOLITHIC, 'Монолитный')
    )

    address = models.TextField(verbose_name='Aдрес')
    number = models.IntegerField(verbose_name='Номер')
    floors = models.IntegerField(verbose_name='Количество этажей')
    entrances = models.IntegerField(verbose_name='Количество подъездов', blank=True, null=True)
    completion_date = models.DateField(verbose_name='Дата сдачи')
    status = models.TextField(verbose_name='Статус', choices=STATUS_CHOICES, default=COMPLETE)
    house_type = models.TextField(verbose_name='Тип дома', choices=HOUSE_TYPE_CHOICES, default=BRICK)
    project = models.ForeignKey('Project', on_delete=models.PROTECT, null=True)

    class Meta:
        unique_together = ('address', 'number')


class Project(models.Model):
    name = models.TextField(verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

