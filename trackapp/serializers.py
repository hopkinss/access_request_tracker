from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import  CS096,Protocol,Product,FileShare,UserAccess


class ProtocolSerializer(serializers.ModelSerializer):
    class Meta:
        model =Protocol
        fields='__all__'


class ProductSerializer(serializers.ModelSerializer):
    protocols=ProtocolSerializer(many=True)

    class Meta:
        model =Product
        fields=('id','product','protocols')


