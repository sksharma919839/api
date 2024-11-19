from rest_framework import serializers
from .models import *


class aboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = about
        fields = "__all__"


class projecctHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = projectHome
        fields = "__all__"


class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = project
        fields = "__all__"


class cvSerializer(serializers.ModelSerializer):
    class Meta:
        model = cv
        fields = "__all__"


class contactSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    phoneNumber = serializers.CharField()
    message = serializers.CharField()
