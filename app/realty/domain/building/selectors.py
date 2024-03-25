from django.core.exceptions import ObjectDoesNotExist

from realty.domain.building.repository import BuildingRepository


class BuildingListSelector:
    def list_building(self):
        return BuildingRepository().get_list()


class BuildingDetailSelector:
    def detail_building(self, pk):
        try:
            return BuildingRepository().get_detail(pk)
        except ObjectDoesNotExist:
            raise
