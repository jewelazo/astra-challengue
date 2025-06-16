from rest_framework import generics
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer, TaskStatusUpdateSerializer
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
    
class TaskApiView(generics.GenericAPIView):
    """
    API view to list tasks.
    """
    def get(self, request):
        status_param = request.query_params.get('status')
        tasks = Task.objects.all()
        if status_param is not None:
            tasks = tasks.filter(status=status_param)
        tasks_serializer = TaskSerializer(tasks, many=True)
        return Response(tasks_serializer.data, status=status.HTTP_200_OK)
    

class TaskDetailAPIView(generics.GenericAPIView):
    """
    API view to get a specific task by ID.
    """
    def patch(self, request, pk=None):
        task = Task.objects.filter(pk=pk).first()
        if task:
            task_serializer = TaskStatusUpdateSerializer(task, data=request.data)
            if task_serializer.is_valid():
                task_serializer.save()
                return Response(TaskSerializer(task).data, status=status.HTTP_200_OK)
            return Response(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Does not exist that id task"}, status=status.HTTP_400_BAD_REQUEST)