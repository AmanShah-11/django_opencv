from rest_framework import serializers
from .models import UserAccessModel


class UserAccessSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserAccessModel
        fields = ('id', 'source_file', 'target_file', 'loggedin')
