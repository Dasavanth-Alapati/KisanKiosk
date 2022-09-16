from rest_framework import serializers
from base.models import RoleRequest
from profilemanager.serializers import SerializedProfile


class SerializedRoleRequest(serializers.ModelSerializer):
    profileid = SerializedProfile(read_only=True)

    class Meta:
        model = RoleRequest
        fields = '__all__'
