from realty.models.project import Project
from realty.domain.common_repository import BaseRepository


class ProjectRepository(BaseRepository):
    model = Project
