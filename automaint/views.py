from django.shortcuts import render
from .models import Car, Maint
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CarSerializer, MaintSerializer

# Create your views here.

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.AllowAny]
    
class MaintViewSet(viewsets.ModelViewSet):
    queryset = Maint.objects.all()
    serializer_class = MaintSerializer
    permission_classes = [permissions.AllowAny]
    