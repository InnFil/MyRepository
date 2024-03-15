from django.urls import path

from realty.views import FlatListAPI, FlatDetailAPI, FloorDetailAPI, BuildingListAPI, BuildingDetailAPI, \
    ProjectListAPI, ProjectDetailAPI

urlpatterns = [
    path('flats/', FlatListAPI.as_view()),
    path('flats/<int:pk>', FlatDetailAPI.as_view()),
    path('floors/<int:pk>', FloorDetailAPI.as_view()),
    path('building/', BuildingListAPI.as_view()),
    path('building/<int:pk>', BuildingDetailAPI.as_view()),
    path('projects/', ProjectListAPI.as_view()),
    path('projects/<int:pk>', ProjectDetailAPI.as_view()),
]
