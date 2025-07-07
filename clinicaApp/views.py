from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import viewsets
from .models import Paciente, HistoriaClinica
from .serializers import PacienteSerializer, HistoriaClinicaSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

    @action(detail=True, methods=['get'])
    def historias(self, request, pk=None):
        paciente = self.get_object()
        historias = paciente.historias_clinicas.all()
        serializer = HistoriaClinicaSerializer(historias, many=True)
        return Response(serializer.data)

class HistoriaClinicaViewSet(viewsets.ModelViewSet):
    queryset = HistoriaClinica.objects.all()
    serializer_class = HistoriaClinicaSerializer
