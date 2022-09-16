from rest_framework import serializers
from base.models import Comment
from profilemanager.serializers import SerializedProfile
from likehandler.serializers import SerializedLike
from posthandler.serializers import SerializedPost
from listingmanager.serializers import SerializedListing
from .serializers import SerializedComment


class SerializedMainComment(serializers.ModelSerializer):
    profileid = SerializedProfile(read_only = True)
    like = SerializedLike(read_only = True)
    comment = SerializedComment(read_only = True,many = True)
    postid = SerializedPost(read_only=True)
    listingid = SerializedListing(read_only=True)
    commentid = SerializedComment(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'