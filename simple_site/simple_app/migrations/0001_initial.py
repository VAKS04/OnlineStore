# Generated by Django 4.2.4 on 2024-05-11 08:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Категории',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('slug', models.SlugField(blank=True)),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Изображение')),
                ('year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1990), django.core.validators.MaxValueValidator(2024)], verbose_name='Год выпуска')),
                ('description', models.TextField(blank=True, max_length=255, verbose_name='Описание')),
                ('bluetoth', models.FloatField(default=4.0, validators=[django.core.validators.MinValueValidator(3.0), django.core.validators.MaxValueValidator(5.5)], verbose_name='Bluetoth')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='simple_app.category')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='ModelDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Название модели')),
            ],
            options={
                'verbose_name': 'Модель',
                'verbose_name_plural': 'Модели ',
            },
        ),
        migrations.CreateModel(
            name='TemplateForLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url_path', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HeadPhone',
            fields=[
                ('device_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='simple_app.device')),
                ('acoustic_design', models.CharField(choices=[('Closed', 'Закрытое'), ('Open', 'Открытое'), ('Half-open', 'Полуоткрытое')], max_length=20, verbose_name='Акустическое оформление')),
                ('lower_limit', models.IntegerField(default=20, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Нижняя граница Гц')),
                ('upper_limit', models.IntegerField(default=20000, validators=[django.core.validators.MinValueValidator(20000), django.core.validators.MaxValueValidator(50000)], verbose_name='Верхняя Граница Гц')),
                ('active_noise_cancellation', models.BooleanField(default=False, verbose_name='Активное шумоподовление')),
            ],
            options={
                'verbose_name': 'Наушники',
                'verbose_name_plural': 'Наушники',
            },
            bases=('simple_app.device',),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('templateforlinks_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='simple_app.templateforlinks')),
            ],
            options={
                'verbose_name': 'Панель меню',
                'verbose_name_plural': 'Панель меню',
            },
            bases=('simple_app.templateforlinks',),
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('device_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='simple_app.device')),
                ('ram', models.IntegerField()),
                ('memory', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Смартфоны',
                'verbose_name_plural': 'Смартфоны',
            },
            bases=('simple_app.device',),
        ),
        migrations.AddField(
            model_name='device',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='simple_app.modeldevice', verbose_name='Модель'),
        ),
        migrations.AddField(
            model_name='device',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype'),
        ),
    ]
