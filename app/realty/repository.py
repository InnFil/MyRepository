from realty.models import Flat, Floor, Building, Project


class BaseRepository:
    model = None

    def get_list(self):
        return self.model.objects.all()

    def get_detail(self, pk):
        return self.model.objects.get(id=pk)


class FlatRepository(BaseRepository):
    model = Flat


class FloorRepository(BaseRepository):
    model = Floor


class BuildingRepository(BaseRepository):
    model = Building


class ProjectRepository(BaseRepository):
    model = Project
