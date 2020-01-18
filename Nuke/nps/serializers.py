from rest_framework import serializers
from .models import NukeList

from django.contrib.auth.models import User

class nuke_Serializer(serializers.ModelSerializer):
    class Meta:
        model = NukeList
        fields = '__all__'

class ToDoUserSerializer(serializers.ModelSerializer):
    pass
    class Meta:
         model = User
         fields = "username", "password"

         extra_kwargs = {'password' : {'write_only' : True}}