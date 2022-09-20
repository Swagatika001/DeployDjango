from rest_framework import serializers
from projects.models import Project
from django.contrib.auth import get_user_model
from .models import StudentSubmission

class AssignmentSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(
                queryset=Project.objects.all())
    student = serializers.PrimaryKeyRelatedField(
                queryset=get_user_model().objects.all())
    url = serializers.CharField(max_length=256)

    def create(self, validated_data):
        return StudentSubmission.objects.create(**validated_data)

    class Meta:
        model = StudentSubmission
        fields = ('id', 'project', 'student',
                  'url', 'feedback', 'approved')
        read_only_fields = ['feedback', 'approved']