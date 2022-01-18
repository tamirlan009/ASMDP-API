from datetime import date
import threading, os
from django.conf import settings
from rest_framework import permissions
from rest_framework import views
from rest_framework.response import Response
from .serializers import UploadDateSerialize
from base.models import UploadDate, DateTable
from .detection.object_detection import Detection

class UploadFilesView(views.APIView):
    """
    Создать запись в таблице 'UploadFiles' и запустить алгоритм обноружения
    """

    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = UploadDateSerialize
    queryset = UploadDate.objects.all()

    def post(self,request):
        serializer_class = UploadDateSerialize(data=request.data)
        if serializer_class.is_valid():
            date_time = request.data['date_value']
            data_table = DateTable(date=date_time)
            data_table.save()
            serializer_class.save(date_table_id=data_table)
            
           
            video = f"{settings.PROJECT_DIR}/{serializer_class.data['video_name']}" 
            
            detect = Detection('object_detection_files\yolov4-tiny.weights', 
                                'object_detection_files\yolov4-tiny.cfg',
                                'object_detection_files\coco.names', 416, date_time
                            )

            t = threading.Thread(target=detect.run, args=(video, data_table,))
            t.setDaemon(True)
            t.start()

            return Response({'success': 'True'})