from django.urls import path

from realty.domain.floor.views import FloorDetailAPI

urlpatterns = [
    path('floors/<int:pk>', FloorDetailAPI.as_view()),
]
