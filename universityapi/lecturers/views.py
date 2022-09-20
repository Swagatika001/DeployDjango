
from django.shortcuts import render
from rest_framework import  viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .serializers import LecturerSerializer

from .models import Lecturer

@permission_classes([IsAuthenticated])
class LecturerViewSet(viewsets.ModelViewSet):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
