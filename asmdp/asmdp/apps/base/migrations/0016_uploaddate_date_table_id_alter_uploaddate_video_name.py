# Generated by Django 4.0.1 on 2022-01-17 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_remove_uploaddate_date_table_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploaddate',
            name='date_table_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='uploaddate', to='base.datetable'),
        ),
        migrations.AlterField(
            model_name='uploaddate',
            name='video_name',
            field=models.FileField(upload_to='upload_files'),
        ),
    ]
