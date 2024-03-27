from unittest import TestCase

from realty.domain.project.selectors import ProjectListSelector, ProjectDetailSelector
from realty.models.project import Project


class BuildingSelectorTest(TestCase):
    def test_list_projects(self):
        project = Project.objects.create(name='Вид на озеро', description='Приятный вид и атмосфера')
        project_2 = Project.objects.create(name='Вид на парк', description='Приятный вид и атмосфера')

        selector_result = ProjectListSelector().list_projects()

        self.assertEqual(len(selector_result), 6)
        print(len(selector_result))
        self.assertIn(project, selector_result)
        self.assertIn(project_2, selector_result)

    def test_detail_project(self):
        project_3 = Project.objects.create(name='Вид на реку', description='Приятный вид и атмосфера')

        selector_result = ProjectDetailSelector().detail_project(pk=project_3.id)

        self.assertEqual(project_3, selector_result)
