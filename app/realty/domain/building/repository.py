from realty.models.building import Building


class BuildingRepository:
    def get_list(self):
        return Building.objects.all()

    def get_detail(self, pk):
        return Building.objects.get(id=pk)
