from unittest import TestCase

from realty.domain.floor.selectors import FloorDetailSelector
from realty.models.floor import Floor


class FloorSelectorTest(TestCase):
    def test_floor_detail(self):
        floor = Floor.objects.create(number=1, color='Бежевый', lighting=Floor.LUMINESCENT)

        selector_result = FloorDetailSelector().floor_detail(pk=floor.id)
        self.assertEqual(floor, selector_result)
