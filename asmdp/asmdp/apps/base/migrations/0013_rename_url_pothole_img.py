# Generated by Django 4.0.1 on 2022-01-12 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_pothole_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pothole',
            old_name='url',
            new_name='img',
        ),
    ]