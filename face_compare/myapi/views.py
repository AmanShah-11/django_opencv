from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# from . import urls
from . import serializers
from . import models
from . import aws_api
from .video import BeginnerVideoFacialDetection


# Create your views here.
class UserAccessViews(viewsets.ModelViewSet):
    serializer_class = serializers.UserAccessSerializers
    queryset = models.UserAccessModel.objects.all()

    def get_queryset(self):
        current_model = ""
        serializer_class = serializers.UserAccessSerializers
        queryset = models.UserAccessModel.objects.all()
        facial_detection = BeginnerVideoFacialDetection()
        source_file, target_file = facial_detection.load_video_camera()
        response, message = aws_api.compare_faces(source_file, target_file)
        if response:
            current_model = models.UserAccessModel.objects.filter(target_file=target_file)
            current_model.source_file = source_file
            current_model.target_file = target_file
            current_model.loggedin = True
            for object in queryset:
                object.save()
        return queryset

