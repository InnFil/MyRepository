from realty.models.project import Project


class ProjectRepository:
    def get_list(self):
        return Project.objects.all()

    def get_detail(self, pk):
        return Project.objects.get(id=pk)
