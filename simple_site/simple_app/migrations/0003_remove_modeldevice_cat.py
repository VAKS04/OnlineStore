# Generated by Django 4.2.4 on 2024-05-13 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple_app', '0002_modeldevice_cat_alter_modeldevice_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modeldevice',
            name='cat',
        ),
    ]
