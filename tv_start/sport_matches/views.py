# from django.shortcuts import render
import requests
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from sport_matches.filters import MatchFilter
from sport_matches.models import *
from sport_matches.serializers import *
from .permissions import IsEditor
from rest_framework.response import Response
class SportTypeViewSet(viewsets.ModelViewSet):
    queryset = SportType.objects.all()
    serializer_class = SportTypeSerializer


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = (IsEditor, )
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MatchFilter

class MatchList(generics.ListAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchViewSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MatchFilter
    def perform_create(self, serializer):
        serializer.save(editor=self.request.user)