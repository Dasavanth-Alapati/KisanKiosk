from rest_framework import serializers
from base.models import Post
from profilemanager.serializers import SerializedProfile
from likehandler.serializers import SerializedLike
from commenthandler.serializers import SerializedComment

class SerializedPost(serializers.ModelSerializer):
    profileid = SerializedProfile(read_only = True)
    like = SerializedLike(read_only = True)
    comment = SerializedComment(read_only = True,many = True)
    class Meta:
        model = Post
        fields = '__all__'
