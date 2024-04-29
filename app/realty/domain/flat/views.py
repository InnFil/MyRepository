from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from realty.domain.flat.selectors import FlatsSelector, FlatDetailSelector


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
