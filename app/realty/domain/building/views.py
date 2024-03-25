from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from realty.domain.building.selectors import BuildingListSelector, BuildingDetailSelector


class BuildingListAPI(APIView):
    class BuildingSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        address = serializers.CharField()
        number = serializers.IntegerField()
        floors = serializers.IntegerField()
        entrances = serializers.IntegerField()
        completion_date = serializers.DateField()
        status = serializers.CharField()
        house_type = serializers.CharField()

    def get(self, request):
        building_list_selector = BuildingListSelector()
        list_building = building_list_selector.list_building()
        data = self.BuildingSerializer(list_building, many=True).data
        return Response(data)


class BuildingDetailAPI(APIView):
    class BuildingSerializer(serializers.Serializer):
        class FlatSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            description = serializers.CharField()
            photo = serializers.ImageField()
            price = serializers.IntegerField()
            square = serializers.IntegerField()
            rooms = serializers.IntegerField()
            number = serializers.IntegerField()
            status = serializers.CharField()

        id = serializers.IntegerField()
        floors = serializers.IntegerField()
        flat_set = FlatSerializer(many=True)

    def get(self, request, pk):
        detail_building_selector = BuildingDetailSelector()
        detail_building = detail_building_selector.detail_building(pk)
        data = self.BuildingSerializer(detail_building).data
        return Response(data)
