# Generated by Django 4.0.1 on 2022-01-17 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_alter_uploaddate_date_table_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploaddate',
            name='video_name',
            field=models.FileField(upload_to='C:\\Users\\admin\\Projects\\ASMDP-API\\asmdp\\asmdp\\media\\upload_files'),
        ),
    ]
