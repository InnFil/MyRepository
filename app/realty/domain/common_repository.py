class BaseRepository:
    model = None

    def get_list(self):
        return self.model.objects.all()

    def get_detail(self, pk):
        return self.model.objects.get(id=pk)
