from django.db import models

class DateTable(models.Model):
    date = models.DateTimeField('date of run detection', default='')
    count_pothole = models.IntegerField('count of pothole detection', default=0)
    count_image = models.IntegerField('count of image save', default=0)
    send_mail_state = models.BooleanField('status sending to mail', default=False)
    url = models.CharField('url of date_table', max_length=300, default='')
    slug = models.CharField('date to slug', max_length=100, default='')
    send_detect = models.BooleanField('value of sending for processing', default=True)
    error_processing = models.BooleanField('error or not to processing', default=False)


    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name = 'Таблица с данными о каждом выезде'
        verbose_name_plural = 'Таблица с данными о каждом выезде'


class Pothole(models.Model):
    url = models.FileField()
    url_txt_file = models.FileField()
    # url = models.CharField('url of image', max_length=500, default='')
    latitude = models.FloatField('latitude location of pothole')
    longitude = models.FloatField('longitude location of pothole')
    count_img_pothole = models.IntegerField('count of pothole detection in image', default=0)
    date_table_id = models.ForeignKey(DateTable, on_delete=models.CASCADE, related_name='pothols')

    def __str__(self):
        return str(self.url)

    class Meta:
        verbose_name = 'Таблица с данными о каждой найденной яме'
        verbose_name_plural = 'Таблица с данными о каждой найденной яме'


class TrackerData(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    navigationtime = models.DateTimeField()
    imei = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Таблица с данными полученные от ГЛОНАСС трекера'
        verbose_name_plural = 'Таблица с данными полученные от ГЛОНАСС трекера'


class UploadDate(models.Model):
    video_name = models.FileField(upload_to='upload_files')   #(upload_to='video/')
    date_value = models.CharField('date of start video', max_length=20)
    date_table_id = models.ForeignKey(DateTable, on_delete=models.CASCADE, related_name='uploaddate')

    def __str__(self):
        return self.date_value

    class Meta:
        verbose_name = 'Таблица с данными полученные о загруженных файлах'
        verbose_name_plural = 'Таблица с данными полученные о загруженных файлах'


class MailNames(models.Model):
    name = models.CharField('name of mail', max_length=100)
    description = models.CharField('description of mail', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Таблица со списком адресов для отправки данных'
        verbose_name_plural = 'Таблица со списком адресов для отправки данных'


class DetectedFile(models.Model):
    title = models.CharField(max_length=100)
    file_path = models.FileField(default='')
    date_table_id = models.ForeignKey(DateTable, on_delete=models.CASCADE, related_name='detectedfile')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Таблица с обработанным файлом'
        verbose_name_plural = 'Таблица с обработанным файлом'



class Notifications(models.Model):
    text = models.CharField('text of notification', max_length=300)

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = 'Таблица, где храняться увидомления'
        verbose_name_plural = 'Таблица, где храняться увидомления'
