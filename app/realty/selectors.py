from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response

from realty.models import Flat, Floor, Building


class FlatsSelector:
    def flats_list(self):
        flats = Flat.objects.all()
        return flats


class FlatDetailSelector:
    def detail_flat(self, pk):
        try:
            flat = Flat.objects.get(id=pk)
            return flat
        except ObjectDoesNotExist:
            return Response(f"Отсутствует квартира с id равным {pk}")


class FloorDetailSelector:
    def detail_floor(self, pk):
        try:
            floor = Floor.objects.get(id=pk)
            return floor
        except ObjectDoesNotExist:
            return Response(f"Отсутствует выбранный этаж")


class BuildingListSelector:
    def building_list(self):
        building = Building.objects.all()
        return building


class BuildingDetailSelector:
    def detail_building(self, pk):
        try:
            building = Building.objects.get(id=pk)
            return building
        except ObjectDoesNotExist:
            return Response(f"Отсутствует выбранный корпус")
