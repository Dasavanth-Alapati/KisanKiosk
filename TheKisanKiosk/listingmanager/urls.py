from django.urls import path
from .views import  apilisting, apimarketplace, createlisting, marketplace, singlelisting

urlpatterns = [
    path('create/',createlisting,name = 'createlisting'),
    path('',marketplace,name='marketplace'),
    path('listing/?P<str:id>/',singlelisting,name='singlelisting'),
    path('apimarketplace/',apimarketplace.as_view()),
    path('apilisting/',apilisting.as_view()),
]
