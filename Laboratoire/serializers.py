from rest_framework import serializers
from Laboratoire.models import LabResearch


class LaboratoireSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabResearch
        fields = '__all__'
