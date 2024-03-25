from django.core.exceptions import ObjectDoesNotExist

from realty.domain.project.repository import ProjectRepository


class ProjectListSelector:
    def list_projects(self):
        return ProjectRepository().get_list()


class ProjectDetailSelector:
    def detail_project(self, pk):
        try:
            return ProjectRepository().get_detail(pk)
        except ObjectDoesNotExist:
            raise
