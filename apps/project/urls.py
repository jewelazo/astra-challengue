from django.urls import path
from .views import ProjectDetailAPIView

urlpatterns = [
    path("project/<int:pk>/",ProjectDetailAPIView.as_view(),name="project_detail_api_view"),

]