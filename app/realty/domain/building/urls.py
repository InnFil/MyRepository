from django.urls import path

from realty.domain.building.views import BuildingListAPI, BuildingDetailAPI

urlpatterns = [
    path('building/', BuildingListAPI.as_view()),
    path('building/<int:pk>', BuildingDetailAPI.as_view()),
]
