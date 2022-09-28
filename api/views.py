from rest_framework import viewsets
from .models import Pii
from .serializers import PiiSerializer

class PiiViewSet(viewsets.ModelViewSet):
    queryset = Pii.objects.all()
    serializer_class = PiiSerializer