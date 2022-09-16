from django.urls import path
from .views import continueorder, merchantordersapi, myorders, myordersapi, orderapi, orderstatus, startorder,merchantorders

urlpatterns = [
    path('order/?P<str:id>/',startorder,name = 'startorder'),
    path('myorders/',myorders,name = 'myorders'),
    path('merchantorders/',merchantorders,name = 'merchantorders'),
    path('reorder/?P<str:id>/',continueorder,name='continueorder'),
    path('orderstatus/?P<str:id>/',orderstatus,name= 'orderstatus'),
    path('apimyorders/',myordersapi.as_view()),
    path('apimerchantorders/',merchantordersapi.as_view()),
    path('apiorder/',orderapi.as_view()),
]
