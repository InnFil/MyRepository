from django.urls import path
from realty.views import FlatListAPI
from realty.views import FlatDetailAPI
from realty.views import FloorDetailAPI
from realty.views import BuildingListAPI
from realty.views import BuildingDetailAPI

urlpatterns = [
    path('flats/', FlatListAPI.as_view()),
    path('flats/<int:pk>', FlatDetailAPI.as_view()),
    path('floors/<int:pk>', FloorDetailAPI.as_view()),
    path('building/', BuildingListAPI.as_view()),
    path('building/<int:pk>', BuildingDetailAPI.as_view()),
]
