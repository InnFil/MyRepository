from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from realty.models import Flat, Floor, Building
from django.db.models import ObjectDoesNotExist


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
        flats = Flat.objects.all()
        data = self.FlatSerializer(flats, many=True).data
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
        try:
            flat = Flat.objects.get(id=pk)
            data = self.FlatSerializer(flat).data
            return Response(data)
        except ObjectDoesNotExist:
            return Response(f"Отсутствует квартира с id равным {pk}")


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
        try:
            floor = Floor.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(f"Отсутствует выбранный этаж")
        data = self.FloorSerializer(floor).data
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
        building = Building.objects.all()
        data = self.BuildingSerializer(building, many=True).data
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
        try:
            building = Building.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(f"Отсутствует выбранный корпус")
        data = self.BuildingSerializer(building).data
        return Response(data)
