# Generated by Django 3.1.2 on 2020-10-28 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201023_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='foto_mascota',
            field=models.ImageField(blank=True, upload_to='api/resources/mascotas'),
        ),
    ]
