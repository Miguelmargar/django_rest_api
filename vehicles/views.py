from django.shortcuts import render
from serializers import VehicleSerializer
from rest_framework import viewsets

# Create your views here.

@api_view(["GET"])
def api_root


class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer