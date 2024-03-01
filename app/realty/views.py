
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from realty.models import Flat
from django.db.models import ObjectDoesNotExist


class FlatListAPI(APIView):
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