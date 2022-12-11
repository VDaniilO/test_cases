from rest_framework import serializers
from .models import *


class PhotoSerializers(serializers.Serializer):
    photo = serializers.ImageField()
    geo_locate = serializers.CharField(max_length=200)
    description = serializers.CharField()
    people_on_photo = serializers.CharField()

    def create(self, validated_data):
        return PhotoModel.objects.create(**validated_data)
