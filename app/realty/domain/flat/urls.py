from django.urls import path

from realty.domain.flat.views import FlatListAPI, FlatDetailAPI

urlpatterns = [
    path('', FlatListAPI.as_view()),
    path('<int:pk>/', FlatDetailAPI.as_view()),
]
