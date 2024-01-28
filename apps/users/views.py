from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .models import UserAbstract
from .serializers import UserAbstractSerializer
# Create your views here.

class UserAbstractList(APIView):
    def get(self, request):
        user = UserAbstract.objects.all()
        serializer = UserAbstractSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserAbstractSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


