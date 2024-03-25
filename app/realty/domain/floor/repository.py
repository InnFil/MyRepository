from realty.models.floor import Floor


class FloorRepository:
    model = None

    def get_list(self):
        return Floor.objects.all()

    def get_detail(self, pk):
        return Floor.objects.get(id=pk)
