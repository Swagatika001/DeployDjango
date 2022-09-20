from django.urls import path, include
from rest_framework import routers
from .views import LecturerViewSet

router = routers.DefaultRouter()
router.register('lecturer', LecturerViewSet,basename='lecturer')

urlpatterns = [
    path('', include(router.urls)),
]