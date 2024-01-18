from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import Services
from .serializers import ServicesSerializer
from .pagination import SmallSetPagination

# Create your views here.


class ServicesList(ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    pagination_class = SmallSetPagination

