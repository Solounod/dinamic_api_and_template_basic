from rest_framework import serializers
from .models import UserAbstract

class UserAbstractSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAbstract
        fields = '__all__'