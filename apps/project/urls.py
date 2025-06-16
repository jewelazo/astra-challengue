from django.urls import path
from .views import ProjectDetailAPIView, TaskApiView, TaskDetailAPIView

urlpatterns = [
    path("project/<int:pk>/",ProjectDetailAPIView.as_view(),name="project_detail_api_view"),
    path("tasks/", TaskApiView.as_view(), name="task_api_view"),
    path("tasks/<int:pk>/", TaskDetailAPIView.as_view(), name="task_detail_api_view"),

]