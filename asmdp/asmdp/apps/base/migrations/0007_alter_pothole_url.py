# Generated by Django 4.0.1 on 2022-01-11 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_pothole_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pothole',
            name='url',
            field=models.CharField(max_length=500, unique=True, verbose_name='url of image'),
        ),
    ]