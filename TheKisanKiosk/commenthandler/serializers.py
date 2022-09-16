from rest_framework import serializers
from base.models import Comment
from profilemanager.serializers import SerializedProfile
from likehandler.serializers import SerializedLike


class SerializedComment(serializers.ModelSerializer):
    profileid = SerializedProfile(read_only = True)
    like = SerializedLike(read_only = True)
    class Meta:
        model = Comment
        fields = '__all__'

