from dataclasses import field
from rest_framework import serializers
from base.models import UploadDate


class UploadDateSerialize(serializers.ModelSerializer):
    """
    Сериалайзер таблицы 'UploadDate'
    """
    
    class Meta:
        model = UploadDate
        # fields="__all__
        exclude = ('date_table_id',)