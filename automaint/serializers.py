from .models import Car, Maint
from rest_framework import serializers

        
class MaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maint
        fields = '__all__'
        
class CarSerializer(serializers.ModelSerializer):
    maintenance = MaintSerializer(many = True, read_only=True)
    class Meta:
        model = Car
        fields = '__all__'