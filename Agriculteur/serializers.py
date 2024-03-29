from rest_framework import serializers
from Agriculteur.models import Farmer


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'
