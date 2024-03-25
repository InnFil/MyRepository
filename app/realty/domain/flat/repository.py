from realty.models.flat import Flat


class FlatRepository:
    def get_list(self):
        return Flat.objects.all()

    def get_detail(self, pk):
        return Flat.objects.get(id=pk)
