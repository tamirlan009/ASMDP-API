from dataclasses import field
from rest_framework import serializers
from .models import DateTable, Pothole
from detect.serializers import UploadDateSerialize



class PotholeTableSerialize(serializers.ModelSerializer):
    """
    Сериалайзер талбицы 'Pothole'
    """
    url = serializers.SerializerMethodField()
    class Meta:
        model = Pothole
        fields = '__all__'

    def get_url(self, pothole):
        request = self.context.get('request')
        url = pothole.url.url
        return request.build_absolute_uri(url)

    # url = serializers.SerializerMethodField()

    # class Meta:
    #     model = Pothole
    #     fields = ('url',) 

    # def get_url(self, pothole):
    #     request = self.context.get('request')
    #     photo = pothole.url.url
    #     return request.build_absolute_uri(photo)

    # url = serializers.SerializerMethodField()

    # class Meta:
    #     model = Pothole
    #     fields = '__all__'

    # def get_days_since_joined(self, obj):
    #     return (now() - obj.date_joined).days





class DateTableSerialize(serializers.ModelSerializer):
    """
    Сериалайзер таблицы 'DateTable' без связанных таблиц
    """

    class Meta:
        model = DateTable
        exclude = ('url','slug')


class DateTableDetailSerialize(serializers.ModelSerializer):
    """
    Сериалайзер таблицы 'DateTable' со связанными таблицами
    """

    pothols = PotholeTableSerialize(many=True)
    uploaddate = UploadDateSerialize(many=True)
    class Meta:
        model = DateTable
        fields = '__all__'
       

class SendMailSerializer(serializers.ModelSerializer):

    pothols = PotholeTableSerialize(many=True)
    class Meta:
        model = DateTable
        fields = ('pothols',)

#  class Meta:
#         models = DateTable
#         fields = '__all__'



# class DateTableSerialize(serializers.ModelSerializer):

#     # pothole = Pothole.objects.all()

#     class Meta:
#         model = DateTable
#         fields = '__all__'
#         # fields = ('id', 'date', 'count_pothole', 'count_image', 'send_mail_state', 'url', 'slug', 'send_detect', 'error_processing')
#         # lookup_field = 'id'
#         # extra_kwargs = {
#         #     'url': {'lookup_field': 'id'}
#         # }

# # class PotholeSerialize(serializers.ModelSerializer):
# #     class Meta:
# #         models = Pothole
# #         fields = '__all__'


# class PotholeSerialize(serializers.ModelSerializer):

#     # date_table_id = serializers.SlugRelatedField(slug_field='date', read_only=True)

#     class Meta:
#         model = Pothole
#         fields = '__all__'
       
      



# class DaySerialize(serializers.ModelSerializer):

#     pothols = PotholeSerialize(many=True)

#     class Meta:
#         model = DateTable
#         fields = '__all__'
#         # exclude = ('id',)