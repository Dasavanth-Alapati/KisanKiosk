from rest_framework import serializers
from base.models import Credentials
from django.contrib.auth.models import User


class SerializedCredentials(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']
