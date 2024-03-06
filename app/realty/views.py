
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from realty.models import Flat, Floor
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
        floor = serializers.IntegerField()
        number = serializers.IntegerField()
        status = serializers.CharField()

    def get(self, request, pk):
        try:
            flat = Flat.objects.get(id=pk)
            data = self.FlatSerializer(flat).data
            return Response(data)
        except ObjectDoesNotExist:
            return Response(f"Отсутствует квартира с id равным {pk}")


class FloorInformationAPI(APIView):
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
        floors = Floor.objects.get(id=pk)
        data = self.FloorSerializer(floors).data
        return Response(data)
