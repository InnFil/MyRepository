from django.urls import path

from realty.domain.building.views import BuildingListAPI, BuildingDetailAPI

urlpatterns = [
    path('', BuildingListAPI.as_view()),
    path('<int:pk>/', BuildingDetailAPI.as_view()),
]
