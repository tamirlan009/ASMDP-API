from django.contrib import admin
from .models import DateTable, Pothole, TrackerData, UploadDate, MailNames, DetectedFile, Notifications


admin.site.register([DateTable, Pothole, TrackerData, UploadDate, MailNames, DetectedFile, Notifications])
