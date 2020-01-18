from rest_framework import serializers
from .models import ATE_Employees

class ATE_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ATE_Employees
        fields = '__all__'
