from django.db import models


class Project(models.Model):
    name = models.TextField(verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(verbose_name='Фото', upload_to="photos/%Y/%m/%d/", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
