from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from realty.domain.project.selectors import ProjectListSelector, ProjectDetailSelector
from realty.models import Building


class ProjectListAPI(APIView):
    class ProjectSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        description = serializers.CharField()

    def get(self, request):
        projects_selector = ProjectListSelector()
        list_projects = projects_selector.list_projects()
        data = self.ProjectSerializer(list_projects, many=True).data
        return Response(data)


class ProjectDetailAPI(APIView):
    class ProjectSerializer(serializers.Serializer):
        class BuildingSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            completion_date = serializers.DateField()
            flat_count = serializers.SerializerMethodField()

            def get_flat_count(self, instance: Building):
                return instance.flat_set.count()

        id = serializers.IntegerField()
        name = serializers.CharField()
        description = serializers.CharField()
        buildings = BuildingSerializer(source='building_set', many=True)

    def get(self, request, pk):
        project = ProjectDetailSelector().detail_project(pk)
        data = self.ProjectSerializer(project).data
        return Response(data)
