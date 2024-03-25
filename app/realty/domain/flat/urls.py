from django.urls import path

from realty.domain.flat.views import FlatListAPI, FlatDetailAPI

urlpatterns = [
    path('flats/', FlatListAPI.as_view()),
    path('flats/<int:pk>', FlatDetailAPI.as_view()),
]
