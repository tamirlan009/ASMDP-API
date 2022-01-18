from django.urls import path
from rest_framework import views
from . import views


urlpatterns = [
    path('get/day', views.DayGetView.as_view()),
    # path('get/day/<int:pk>/', views.DayDetileGetVeiw.as_view()),
    path('get/photols/<int:pk>', views.GetPotholeGetView.as_view()),
    path('delete/day/<int:pk>', views.DayDeliteView.as_view()),
    path('delete/img/<int:pk>', views.ImageDeliteView.as_view()),
    path('sendmail/<int:pk>', views.SendMail.as_view()),
]


