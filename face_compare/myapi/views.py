from django.shortcuts import render
from rest_framework import viewsets
# from . import urls
from . import serializers
from . import models
from . import aws_api
from .video import BeginnerVideoFacialDetection


# Create your views here.
class UserAccessViews(viewsets.ModelViewSet):
    serializer_class = serializers.UserAccessSerializers
    queryset = models.UserAccessModel.objects.all()

    def post(self, request):
        if request.method == "POST":
            source_file, target_file = BeginnerVideoFacialDetection.load_video_camera()
            response, message = aws_api.compare_faces(source_file, target_file)
            if response:
                current_model = models.UserAccessModel.objects.filter(target_file=target_file)
                current_model.loggedin = True
