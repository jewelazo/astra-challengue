from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer
from rest_framework import generics, status
from rest_framework.response import Response
# Create your views here.

class ProjectDetailAPIView(generics.GenericAPIView):
    """
    API view tasks for a specific project.
    """
    def get(self, request, pk=None):
        project = Project.objects.filter(pk=pk).first()
        if project:
            project_serializer = ProjectSerializer(project)
            return Response(project_serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "Does not exist that id project"}, status=status.HTTP_400_BAD_REQUEST)
