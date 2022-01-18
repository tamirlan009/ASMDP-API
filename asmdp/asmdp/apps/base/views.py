from array import array
import os, shutil, zipfile
from rest_framework import permissions
from rest_framework import generics
from rest_framework import views
from rest_framework import status
from django.conf import settings
from rest_framework.response import Response
from .serializers import DateTableSerialize, DateTableDetailSerialize, PotholeTableSerialize, SendMailSerializer
from .models import DateTable, Pothole


class DayGetView(generics.ListAPIView):
    """
    Получить все записи таблицы 'DateTable' без связанных таблиц
    """

    queryset = DateTable.objects.all()
    serializer_class = DateTableSerialize
    permission_classes = [permissions.IsAuthenticated]



class GetPotholeGetView(views.APIView):
    """
    Получить все записи с таблицы 'Pothole' по id 'DateTable'
    """
    
    permission_classes = [permissions.IsAuthenticated]
   
    def get(self, request, pk):
        pothole = Pothole.objects.filter(date_table_id = pk)
        serializer = PotholeTableSerialize(pothole, context={"request": request}, many=True)

        return Response(serializer.data)


    
class DayDeliteView(generics.DestroyAPIView):
    """
    Удалить одну запись с таблицы 'DateTable' 
    """
    
    permission_classes = [permissions.IsAuthenticated]
    queryset = DateTable.objects.all()
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        video_url = instance.uploaddate.first().video_name
        day_path = instance.url 
        detected_video_url = instance.detectedfile.first().file_path
     
        
        try:
            os.remove(f'{settings.MEDIA_ROOT}/{video_url}')
            os.remove(str(detected_video_url))
            shutil.rmtree(str(day_path))
        except:
            pass

        self.perform_destroy(instance)

        return Response(status=status.HTTP_204_NO_CONTENT)



class ImageDeliteView(generics.DestroyAPIView):
    """
    Удалить одну запись с таблицы 'Pothole'
    """
    
    permission_classes = [permissions.IsAuthenticated]
    queryset = Pothole.objects.all()
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        img = instance.url
        txt = instance.url_txt_file
        try:
            os.remove(f'{settings.MEDIA_ROOT}/{img}')
            os.remove(f'{settings.MEDIA_ROOT}/{txt}')
        except:
            pass

        self.perform_destroy(instance)
    
        return Response(status=status.HTTP_204_NO_CONTENT)


class SendMail(views.APIView):

    permission_classes = [permissions.IsAuthenticated]
    

    def post(self, request, pk):

        queryset = DateTable.objects.filter(id = pk).first()
        
        """
        Создание ZIP архива 
        """
        pothols = queryset.pothols.all()
        mail = request.data['mail']
        
        zip_path = f'{settings.MEDIA_ROOT}/{str(queryset.url)}'
        max_zip_size = 18
        real_size = 0
        count_zip = 0

        zip_file_nam = os.path.join(zip_path, f'{queryset.slug}_{count_zip}.zip')
        zp = zipfile.ZipFile(zip_file_nam, 'w')

        for i in pothols:
            print(i.url)
            print(i.url_txt_file)
        # pothols = queryset
        # serializer = SendMailSerializer(self.queryset, many=True)
        
        # print(serializer.data)
        
        # instance = self.get_object()
        # pothols = instance.pothols.all()

        # for i in pothols:       
        #     print(os.path.join(settings.MEDIA_ROOT, str(i.url)))
        #     print(os.path.join(settings.MEDIA_ROOT, str(i.url_txt_file)))
        
        # mail = request.data['mail']

       

        # zip_size = 18
        # path_size = 0
        # count_zip = 1


        return Response({'yes':'yes'})


# class SendMail(generics.RetrieveAPIView):

#     queryset = DateTable.objects.all()
#     serializer_class = DateTableDetailSerialize
#     permission_classes = [permissions.IsAuthenticated]

#     def retrieve(self, request, *args, **kwargs):

#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         pothols = instance.pothols.all()
#         for i in pothols:       
#             print(os.path.join(settings.MEDIA_ROOT, str(i.url)))
#             print(os.path.join(settings.MEDIA_ROOT, str(i.url_txt_file)))
    
#         return Response(serializer.data)