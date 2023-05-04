# from django.shortcuts import render
import requests
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from sport_matches.filters import MatchFilter
from sport_matches.models import *
from sport_matches.serializers import *
from .permissions import IsEditor

class SportTypeViewSet(viewsets.ModelViewSet):
    queryset = SportType.objects.all()
    serializer_class = SportTypeSerializer


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = (IsEditor, )

class MatchList(generics.ListAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MatchFilter
    def perform_create(self, serializer):
        serializer.save(editor=self.request.user)