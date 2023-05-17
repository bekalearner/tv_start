from rest_framework import generics, filters, viewsets

from tv_start.permissions import IsEditor
from .models import *
from .serializers import BackgammonSerializer, BackgammonViewSerializer
from rest_framework.permissions import IsAdminUser

class BackgammonViewSet(viewsets.ModelViewSet):
    queryset = Backgammon.objects.all()
    serializer_class = BackgammonViewSerializer
    permission_classes = (IsEditor,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'tournament__name')


class BackgammonList(generics.ListAPIView):
    queryset = Backgammon.objects.all()
    serializer_class = BackgammonSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'tournament__name')
