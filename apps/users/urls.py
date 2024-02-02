from django.urls import path
from .views import UserAbstractList, LoginWhitToken


urlpatterns = [
    path('users/', 
        UserAbstractList.as_view(), 
        name='services_list'),
    path('login/', LoginWhitToken.as_view(), name='login')
]
