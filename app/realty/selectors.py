from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count
from rest_framework.response import Response

from realty.models import Flat, Floor, Building, Project


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


class ProjectListSelector:
    def list_projects(self):
        projects = Project.objects.all()
        return projects


class ProjectDetailSelector:
    def detail_project(self, pk):
        try:
            project = Project.objects.get(id=pk)
            return project
        except ObjectDoesNotExist:
            raise


