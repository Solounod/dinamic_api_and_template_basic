from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .models import UserAbstract
from .serializers import UserAbstractSerializer, UserAbstractListSerializer
# Create your views here.

class UserAbstractList(APIView):
    model = UserAbstract
    serializer_class = UserAbstractSerializer
    list_serializer_class = UserAbstractListSerializer
    queryset = None

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects\
                .filter(is_active=True)\
                .values('id', 'username', 'email', 'first_name', 'last_name')
        return self.queryset
        
    def get(self, request):
        users = self.get_queryset()
        users_serializer = self.list_serializer_class(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message': 'Usuario registrado correctamente.'
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'Hay errores en el registro',
            'errors': user_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    

class LoginWhitToken(ObtainAuthToken):
    def post(self, request, *args, **kawargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token' : token.key,
            'user_id': user.pk,
            'email' : user.email,
        })
