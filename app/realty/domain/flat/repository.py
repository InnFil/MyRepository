from realty.models import Flat
from realty.domain.common_repository import BaseRepository


class FlatRepository(BaseRepository):
    model = Flat
