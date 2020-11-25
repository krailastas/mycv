from rest_framework import viewsets

from .models import Main
from .serializers import MainSerializer


class MainViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MainSerializer
    queryset = Main.objects.order_by('-order')
