from datetime import datetime

from django.contrib.sessions.models import Session
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .models import UserAbstract
from .serializers import UserAbstractSerializer, UserAbstractListSerializer, UserAbstractTokenSerializer
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
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                user_serializer = UserAbstractTokenSerializer(user)
                if created:
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Sesión iniciada correctamente.'
                    }, status=status.HTTP_201_CREATED)
                else:
                    all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()
                    token.delete()
                    token = Token.objects.create(user = user)
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Sesión iniciada correctamente.'
                    }, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'Usuario inactivo'},
                                status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors,
                            {'message': 'Usuario o contraseña incorrectos'},
                            status=status.HTTP_400_BAD_REQUEST)
        
class LogoutWhitToken(APIView):
    def get(self, request, *args, **kwargs):
        try:
            token = request.GET.get('token')
            print(token)
            token = Token.objects.filter(key = token).first()
            print(token)
            if token:
                user = token.user
                print(user)
                all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                
                token.delete()
                session_message = 'Sesión cerrada correctamente.'
                token_message = 'Token eliminado correctamente.'
                return Response({'token_message': token_message, 'session_message': session_message},
                                status=status.HTTP_200_OK)
        
            return Response({'message': 'No se ha encontrado el usuario con el token'},
                        status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message': 'No se a encontrado el token'},
                            status=status.HTTP_409_CONFLICT)   
            