from rest_framework import generics, filters, viewsets
from .models import *
from .serializers import BackgammonSerializer, BackgammonViewSerializer


class BackgammonViewSet(viewsets.ModelViewSet):
    queryset = Backgammon.objects.all()
    serializer_class = BackgammonViewSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'tournament__name')


class BackgammonList(generics.ListAPIView):
    queryset = Backgammon.objects.all()
    serializer_class = BackgammonSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'tournament__name')
