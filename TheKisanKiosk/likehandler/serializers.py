from rest_framework import serializers
from base.models import Likeinfo, Like
from profilemanager.serializers import SerializedProfile


class SerializedLikeinfo(serializers.ModelSerializer):
    profileid = SerializedProfile(read_only = True)
    class Meta:
        model = Likeinfo
        fields = '__all__'


class SerializedLike(serializers.ModelSerializer):
    likeinfo = SerializedLikeinfo(read_only=True, many=True)
    class Meta:
        model = Like
        fields = '__all__'
