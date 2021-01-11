from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'allobjects', views.UserAccessViews)

urlpatterns = [
    # path('', views, name='schedule'),
    # path('users', views.users, name='users'),
    path('', include(router.urls)),
    # path('', views.APIView.as_view())
]
