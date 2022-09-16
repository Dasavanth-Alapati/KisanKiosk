from rest_framework import serializers
from base.models import Order
from profilemanager.serializers import SerializedProfile
from listingmanager.serializers import SerializedListing

class SerializedOrder(serializers.ModelSerializer):
    buyerid = SerializedProfile(read_only = True)
    listingid = SerializedListing(read_only = True)
    class Meta:
        model = Order
        fields = '__all__'