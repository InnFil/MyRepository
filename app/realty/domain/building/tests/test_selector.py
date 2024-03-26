from unittest import TestCase

from realty.domain.building.selectors import BuildingDetailSelector, BuildingListSelector
from realty.models.building import Building
from realty.models.project import Project


class BuildingSelectorTest(TestCase):
    def test_list_building(self):
        project = Project.objects.create(name='Вид на озеро 2024', description='Приятный вид и атмосфера')
        building = Building.objects.create(
            address='Сабурова', number=1, floors=5, entrances=2, completion_date='2024-01-01', status=Building.COMPLETE,
            house_type=Building.BRICK, project_id=project.id
        )
        project_2 = Project.objects.create(name='Вид на озеро 2024', description='Приятный вид и атмосфера')
        building_2 = Building.objects.create(
            address='Петрова', number=2, floors=5, entrances=1, completion_date='2024-01-01', status=Building.COMPLETE,
            house_type=Building.PANEL, project_id=project_2.id
        )

        selector_result = BuildingListSelector().list_building()

        self.assertEqual(len(selector_result), 3)
        self.assertIn(building, selector_result)
        self.assertIn(building_2, selector_result)

    def test_building_detail(self):
        project_3 = Project.objects.create(name='Вид на озеро 2024', description='Приятный вид и атмосфера')
        building_3 = Building.objects.create(
            address='Барамзина', number=6, floors=5, entrances=2, completion_date='2024-01-01', status=Building.COMPLETE,
            house_type=Building.BRICK, project_id=project_3.id
        )

        selector_result = BuildingDetailSelector().detail_building(pk=building_3.id)

        self.assertEqual(building_3, selector_result)
