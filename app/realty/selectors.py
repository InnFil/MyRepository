from django.core.exceptions import ObjectDoesNotExist

from realty.Repository import FlatRepository, FloorRepository, BuildingRepository, ProjectRepository


class FlatsSelector:
    def list_flats(self):
        return FlatRepository().get_list()


class FlatDetailSelector:
    def flat_detail(self, pk):
        try:
            return FlatRepository().get_detail(pk)
        except ObjectDoesNotExist:
            raise


class FloorDetailSelector:
    def floor_detail(self, pk):
        try:
            return FloorRepository().get_detail(pk)
        except ObjectDoesNotExist:
            raise


class BuildingListSelector:
    def list_building(self):
        return BuildingRepository().get_list()


class BuildingDetailSelector:
    def detail_building(self, pk):
        try:
            return BuildingRepository().get_detail(pk)
        except ObjectDoesNotExist:
            raise



class ProjectListSelector:
    def list_projects(self):
        return ProjectRepository().get_list()


class ProjectDetailSelector:
    def detail_project(self, pk):
        try:
            return ProjectRepository().get_detail(pk)
        except ObjectDoesNotExist:
            raise
