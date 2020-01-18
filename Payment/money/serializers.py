from rest_framework import serializers
from .models import PayList

class Pay_Serializer(serializers.ModelSerializer):
    class Meta:
        model = PayList
        fields = '__all__'
