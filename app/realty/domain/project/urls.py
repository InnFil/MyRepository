from django.urls import path

from realty.domain.project.views import ProjectListAPI, ProjectDetailAPI

urlpatterns = [
    path('projects/', ProjectListAPI.as_view()),
    path('projects/<int:pk>', ProjectDetailAPI.as_view()),
]
