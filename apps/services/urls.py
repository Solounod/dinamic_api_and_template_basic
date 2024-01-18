from django.urls import path
from .views import ServicesList

urlpatterns = [
    path('services/', ServicesList.as_view(), name='services_list'),
]
