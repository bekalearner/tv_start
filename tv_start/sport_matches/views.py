from django_filters import rest_framework as rest_filters
from rest_framework import viewsets, generics, filters
from sport_matches.filters import MatchFilter
from sport_matches.serializers import *
from tv_start.permissions import *
from rest_framework.permissions import IsAdminUser

class SportTypeViewSet(viewsets.ModelViewSet):
    queryset = SportType.objects.all()
    serializer_class = SportTypeSerializer


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = (Editor, )
    filter_backends = (rest_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = MatchFilter
    search_fields = ('sport_type__name', 'tournament__name', 'team_one__name', 'team_two__name',)


class MatchList(generics.ListAPIView):
    queryset = Match.objects.all().order_by('-created_date')
    serializer_class = MatchViewSerializer
    filter_backends = (rest_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = MatchFilter
    search_fields = ('sport_type__name', 'tournament__name', 'team_one__name', 'team_two__name',)

    def perform_create(self, serializer):
        serializer.save(editor=self.request.user)
