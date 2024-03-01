
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from realty.models import Flat


class FlatListAPI(APIView):
    class FlatSerializer(serializers.Serializer):
        id = serializers.CharField()
        description = serializers.CharField()
        photo = serializers.CharField()
        price = serializers.CharField()
        square = serializers.CharField()
        rooms = serializers.CharField()
        floor = serializers.CharField()
        number = serializers.CharField()
        status = serializers.CharField()

    def get(self, request):
        flats = Flat.objects.all()
        data = self.FlatSerializer(flats, many=True).data
        return Response(data)


class FlatDetailAPI(APIView):
    class FlatSerializer(serializers.Serializer):
        id = serializers.CharField()
        description = serializers.CharField()
        photo = serializers.CharField()
        price = serializers.CharField()
        square = serializers.CharField()
        rooms = serializers.CharField()
        floor = serializers.CharField()
        number = serializers.CharField()
        status = serializers.CharField()

    def get(self, request, pk):
        flat = Flat.objects.get(id=pk)
        data = self.FlatSerializer(flat).data
        return Response(data)
