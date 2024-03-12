from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from realty.models import Flat, Floor, Building
from django.db.models import ObjectDoesNotExist

from realty.selectors import FlatsSelector, FlatDetailSelector, FloorDetailSelector, BuildingListSelector, \
    BuildingDetailSelector


class FlatListAPI(APIView):
    class FlatSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        description = serializers.CharField()
        photo = serializers.ImageField()
        price = serializers.IntegerField()
        square = serializers.IntegerField()
        rooms = serializers.IntegerField()
        floor = serializers.IntegerField(source='floor.number')
        number = serializers.IntegerField()
        status = serializers.CharField()

    def get(self, request):
        flats_selector = FlatsSelector()
        list_flats = flats_selector.list_flats()
        data = self.FlatSerializer(list_flats, many=True).data
        return Response(data)


class FlatDetailAPI(APIView):
    class FlatSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        description = serializers.CharField()
        photo = serializers.ImageField()
        price = serializers.IntegerField()
        square = serializers.IntegerField()
        rooms = serializers.IntegerField()
        floor = serializers.IntegerField(source='floor.number')
        number = serializers.IntegerField()
        status = serializers.CharField()

    def get(self, request, pk):
        flat_detail_selector = FlatDetailSelector()
        flat_detail = flat_detail_selector.flat_detail(pk)
        data = self.FlatSerializer(flat_detail).data
        return Response(data)


class FloorDetailAPI(APIView):
    class FloorSerializer(serializers.Serializer):
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
        number = serializers.IntegerField()
        color = serializers.CharField()
        lighting = serializers.CharField()
        flat_set = FlatSerializer(many=True)

    def get(self, request, pk):
        floor_detail_selector = FloorDetailSelector()
        floor_detail = floor_detail_selector.floor_detail(pk)
        data = self.FloorSerializer(floor_detail).data
        return Response(data)


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

        floors = serializers.IntegerField()
        id = serializers.IntegerField()
        flat_set = FlatSerializer(many=True)

    def get(self, request, pk):
        detail_building_selector = BuildingDetailSelector()
        detail_building = detail_building_selector.detail_building(pk)
        data = self.BuildingSerializer(detail_building).data
        return Response(data)
