from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ("id", "title", "description", "required_skills", "min_experience", "location", "created_by", "created_at")
        read_only_fields = ("created_by", "created_at")