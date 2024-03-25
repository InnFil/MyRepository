from realty.models.building import Building
from realty.domain.common_repository import BaseRepository


class BuildingRepository(BaseRepository):
    model = Building
