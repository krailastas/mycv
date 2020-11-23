from rest_framework import viewsets

from .models import Main, Jobs
from .serializers import MainSerializer, JobsSerializer


class MainViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MainSerializer
    queryset = Main.objects.all()


class JobsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = JobsSerializer
    queryset = Jobs.objects.all()
