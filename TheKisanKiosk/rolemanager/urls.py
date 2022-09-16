
from django.urls import path


from .views import apirolerequest, roledisplay, rolerequest,roleapproval

urlpatterns = [
    path('request/',rolerequest,name='rolerequest'),
    path('display/',roledisplay,name = 'requestdisplay'),
    path('display/?P<str:id>/',roleapproval,name='requestapproval'),
    path('api/',apirolerequest.as_view()),
]
