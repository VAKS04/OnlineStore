# Generated by Django 4.2.4 on 2024-04-21 14:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_app', '0004_headphone_device_bluetoth'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': 'Панель меню', 'verbose_name_plural': 'Панель меню'},
        ),
        migrations.AlterField(
            model_name='headphone',
            name='acoustic_design',
            field=models.CharField(choices=[('Closed', 'Закрытое'), ('Open', 'Открытое'), ('Half-open', 'Полуоткрытое')], max_length=20, verbose_name='Акустическое оформление'),
        ),
        migrations.AlterField(
            model_name='headphone',
            name='lower_limit',
            field=models.IntegerField(default=20, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Нижняя граница Гц'),
        ),
        migrations.AlterField(
            model_name='headphone',
            name='upper_limit',
            field=models.IntegerField(default=20000, validators=[django.core.validators.MinValueValidator(20000), django.core.validators.MaxValueValidator(50000)], verbose_name='Верхняя Граница Гц'),
        ),
    ]
