# from django.shortcuts import render
import requests
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser

from sport_matches.filters import MatchFilter
from sport_matches.models import SportType, Match
from sport_matches.serializers import MatchSerializer, SportTypeSerializer


class SportTypeViewSet(viewsets.ModelViewSet):
    queryset = SportType.objects.all()
    serializer_class = SportTypeSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = (IsAdminUser, )

class MatchList(generics.ListAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MatchFilter
