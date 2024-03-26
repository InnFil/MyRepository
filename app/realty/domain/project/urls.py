from django.urls import path

from realty.domain.project.views import ProjectListAPI, ProjectDetailAPI

urlpatterns = [
    path('<int:pk>/', ProjectDetailAPI.as_view()),
]
