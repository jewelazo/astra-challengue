from rest_framework import serializers
from .models import Project, Task
from datetime import datetime


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model.
    """
    def validate_due_date(self, value):
        """
        Ensure that the due date is not in the past.
        """
        if value and value <= datetime.now().date():
            raise serializers.ValidationError("Due date cannot be in the past, please provide a future date.")
        return value

    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]


class TaskStatusUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer to update only the status of a Task.
    """

    class Meta:
        model = Task
        fields = ["status"]


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for the Project model.
    """

    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ["id", "name", "description", "created_at", "updated_at", "tasks"]
        read_only_fields = ["id", "created_at", "updated_at"]
