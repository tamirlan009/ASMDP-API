from django.urls import path
from rest_framework import views
from . import views


urlpatterns = [
    path('', views.UploadFilesView.as_view()),
]




