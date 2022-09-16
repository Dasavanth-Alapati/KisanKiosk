from django.urls import path
from .views import LikeApi, like,dislike

urlpatterns = [
    path('like/',like,name='like'),
    path('dislike/',dislike,name='dislike'),
    path('apilike/',LikeApi.as_view()),
]
