# serializers.py
from rest_framework import serializers
from .models import Paciente, HistoriaClinica

class HistoriaClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriaClinica
        fields = '__all__'

class PacienteSerializer(serializers.ModelSerializer):
    historias_clinicas = HistoriaClinicaSerializer(many=True, read_only=True)

    class Meta:
        model = Paciente
        fields = '__all__'