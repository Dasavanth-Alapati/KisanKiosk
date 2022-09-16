from rest_framework import serializers
from base.models import Profile
from login.serializers import SerializedCredentials


class SerializedProfile(serializers.ModelSerializer):
    credid = SerializedCredentials(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'
