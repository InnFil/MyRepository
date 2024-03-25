from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from realty.domain.floor.selectors import FloorDetailSelector


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
