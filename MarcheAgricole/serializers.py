from rest_framework import serializers
from MarcheAgricole.models import MarketData


class MarketDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketData
        fields = '__all__'
