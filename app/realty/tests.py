from django.test import TestCase

from realty.selectors import FlatsSelector, FlatDetailSelector
from realty.models import Flat, Floor, Section, Building, Project


class FlatsSelectorTest(TestCase):
    def test_list_flats(self):
        floor = Floor.objects.create(number=2, color='Бежевый', lighting=Floor.DIODE)
        section = Section.objects.create(name='Вид на озеро')
        project = Project.objects.create(name='Вид на озеро 2024', description='Приятный вид и атмосфера')
        building = Building.objects.create(
            address='Петропавловская', number=3, floors=2, entrances=1, completion_date='2024-01-01',
            status=Building.COMPLETE, house_type=Building.BRICK, project_id=project.id
        )
        flat = Flat.objects.create(
            description='ЖК Новый город', price=2800000, square=30, rooms=1,number=22, status=Flat.ON_SALE,
            floor_id=floor.id, section_id=section.id, building_id=building.id
        )
        flat_2 = Flat.objects.create(
            description='ЖК Новый город', price=2800000, square=30, rooms=1, number=21,status=Flat.ON_SALE,
            floor_id=floor.id, section_id=section.id, building_id=building.id
        )

        selector_result = FlatsSelector().list_flats()

        self.assertEqual(len(selector_result), 2)
        self.assertIn(flat, selector_result)
        self.assertIn(flat_2, selector_result)

    def test_flat_detail(self):
        floor = Floor.objects.create(number=2, color='Бежевый', lighting=Floor.DIODE)
        section = Section.objects.create(name='Вид на озеро')
        project = Project.objects.create(name='Вид на озеро 2024', description='Приятный вид и атмосфера')
        building = Building.objects.create(
            address='Петропавловская', number=3, floors=2, entrances=1, completion_date='2024-01-01',
            status=Building.COMPLETE, house_type=Building.BRICK, project_id=project.id
        )
        flat = Flat.objects.create(
            description='ЖК Новый город', price=2800000, square=30, rooms=1, number=22, status=Flat.ON_SALE,
            floor_id=floor.id, section_id=section.id, building_id=building.id
        )

        selector_result = FlatDetailSelector().flat_detail(pk=flat.id)

        self.assertEqual(flat, selector_result)
