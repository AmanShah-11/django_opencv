from rest_framework import serializers
from .models import UserAccessModel


class UserAccessSerializers(serializers.ModelSerializer):
    allowed = serializers.SerializerMethodField()

    def get_allowed(self):
        pass
