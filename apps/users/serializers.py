from rest_framework import serializers
from .models import UserAbstract

class UserAbstractSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAbstract
        fields = '__all__'

    def create(self, validated_data):
        
        
        user = UserAbstract.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()


        return user
    
class UserAbstractListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAbstract
        
    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email'],
            'first_name': instance['first_name'],
            'last_name': instance['last_name'],
        } 