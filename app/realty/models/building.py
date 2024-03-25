from django.db import models


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
    photo = models.ImageField(verbose_name='Фото', upload_to="photos/%Y/%m/%d/", blank=True, null=True)
    floors = models.IntegerField(verbose_name='Количество этажей')
    entrances = models.IntegerField(verbose_name='Количество подъездов', blank=True, null=True)
    completion_date = models.DateField(verbose_name='Дата сдачи')
    status = models.TextField(verbose_name='Статус', choices=STATUS_CHOICES, default=COMPLETE)
    house_type = models.TextField(verbose_name='Тип дома', choices=HOUSE_TYPE_CHOICES, default=BRICK)
    project = models.ForeignKey('Project', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.house_type

    class Meta:
        unique_together = ('address', 'number')
        verbose_name = 'Корпус'
        verbose_name_plural = 'Корпуса'
