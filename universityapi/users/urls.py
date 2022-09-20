from django.urls import path, include
from rest_framework import routers

from .views import (
    UserViewSet, SubmissionsViewSet, CustomAuthToken, UserProfileView
)

router = routers.DefaultRouter()
router.register('user', UserViewSet,basename='user')

router.register('submissions',SubmissionsViewSet,basename='submissions')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/profile/',
         UserProfileView.as_view(), name='user-profile'),
    path('login', CustomAuthToken.as_view()),
    # path('authorize', CustomAuthToken.as_view()),
]