from django.core.exceptions import ObjectDoesNotExist

from realty.domain.floor.repository import FloorRepository


class FloorDetailSelector:
    def floor_detail(self, pk):
        try:
            return FloorRepository().get_detail(pk)
        except ObjectDoesNotExist:
            raise
