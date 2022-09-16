from django.urls import path
from .views import apifetchposts, apisinglepost, postdisplay,createpost, singlepost

urlpatterns = [
    path('feed/',postdisplay,name = 'postdisplay'),
    path('create/',createpost,name='createpost'),
    path('post/?P<str:id>/',singlepost,name = 'singlepost'),
    path('apifeed/',apifetchposts.as_view()),
    path('apipost/',apisinglepost.as_view()),
]
