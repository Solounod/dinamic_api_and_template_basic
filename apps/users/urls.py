from django.urls import path
from .views import UserAbstractList


urlpatterns = [
    path('get/', 
        UserAbstractList.as_view(), 
        name='services_list'),
]
