from django.shortcuts import render
from rest_framework import  viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .serializers import CertificateSerializer

from .models import Certificate

@permission_classes([IsAuthenticated])
class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer