from django.shortcuts import render
from rest_framework import viewsets
from . import urls
from . import serializers
from . import models


# Create your views here.
class UserAccessModels(viewsets.ModelViewSet):
    serializer_class = serializers.UserAccessSerializers
    queryset = models.UserAccessModels.objects.all()