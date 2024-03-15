# Generated by Django 5.0.2 on 2024-03-15 09:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0005_project_building_project'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='building',
            options={'verbose_name': 'Корпус', 'verbose_name_plural': 'Корпуса'},
        ),
        migrations.AlterModelOptions(
            name='floor',
            options={'verbose_name': 'Этаж', 'verbose_name_plural': 'Этажи'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'verbose_name': 'Cекция', 'verbose_name_plural': 'Секции'},
        ),
        migrations.AlterField(
            model_name='flat',
            name='building',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='realty.building', verbose_name='Корпус'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='floor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='realty.floor', verbose_name='Этаж'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='realty.section', verbose_name='Секция'),
        ),
    ]