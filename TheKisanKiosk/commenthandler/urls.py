from django.urls import path
from . views import commentapi, createcomment, singlecomment

urlpatterns = [
    path('createcomment/?P<str:id>/?P<str:type>/',createcomment,name='createcomment'),
    path('singlecomment/?P<str:id>/',singlecomment,name='singlecomment'),
    path('apicomment/',commentapi.as_view()),
]
