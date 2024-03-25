from django.core.exceptions import ObjectDoesNotExist

from realty.domain.flat.repository import FlatRepository


class FlatsSelector:
    def list_flats(self):
        return FlatRepository().get_list()


class FlatDetailSelector:
    def flat_detail(self, pk):
        try:
            return FlatRepository().get_detail(pk)
        except ObjectDoesNotExist:
            raise
