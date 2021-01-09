from django.urls import path, include
from rest_framework import routers

from . import views

urlpatterns = [
    path('', views, name='schedule'),
    # path('users', views.users, name='users'),
    # path('', include(router.urls))
]