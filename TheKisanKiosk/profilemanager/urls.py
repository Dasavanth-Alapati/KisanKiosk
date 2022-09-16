from django.urls import path
from .views import apiprofile, addmoney, apimoney, profiledisplay, profileedit
from rest_framework.decorators import api_view

urlpatterns = [
    path('display/',profiledisplay,name='profiledisplay'),
    path('edit/',profileedit,name='profileedit'),
    path('display/?P<str:id>/',profiledisplay,name='otherprofiledisplay'),
    path('addmoney/',addmoney,name = 'addmoney'),
    path('apiprofile/',apiprofile.as_view()),
    path('apimoney/',apimoney.as_view()),
]
