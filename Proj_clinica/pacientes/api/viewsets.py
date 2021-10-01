from rest_framework import viewsets

from pacientes.models import Pacientes
from pacientes.api.serializers import PacientesSerializer

class PacientesViewSets(viewsets.ModelViewSet): 
    queryset = Pacientes.objects.all()
    serializer_class = PacientesSerializer