
from django.urls import path
from .views import apilogin
from rest_framework.decorators import api_view

urlpatterns = [
    path('',apilogin.as_view())
]
