from rest_framework import serializers
from base.models import Listing
from profilemanager.serializers import SerializedProfile
from likehandler.serializers import SerializedLike
from commenthandler.serializers import SerializedComment


class SerializedListing(serializers.ModelSerializer):
    sellerid = SerializedProfile(read_only = True)
    like = SerializedLike(read_only = True)
    comment = SerializedComment(read_only = True,many = True)
    class Meta:
        model = Listing
        fields = '__all__'