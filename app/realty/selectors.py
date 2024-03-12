from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response

from realty.models import Flat, Floor, Building


class FlatsSelector:
    def list_flats(self):
        flats = Flat.objects.all()
        return flats


class FlatDetailSelector:
    def flat_detail(self, pk):
        try:
            flat = Flat.objects.get(id=pk)
            return flat
        except ObjectDoesNotExist:
            raise


class FloorDetailSelector:
    def floor_detail(self, pk):
        try:
            floor = Floor.objects.get(id=pk)
            return floor
        except ObjectDoesNotExist:
            raise


class BuildingListSelector:
    def list_building(self):
        building = Building.objects.all()
        return building


class BuildingDetailSelector:
    def detail_building(self, pk):
        try:
            building = Building.objects.get(id=pk)
            return building
        except ObjectDoesNotExist:
            raise
