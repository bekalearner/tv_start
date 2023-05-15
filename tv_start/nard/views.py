from rest_framework import generics, filters, viewsets
from .models import *
from .serializers import BackgammonSerializer, BackgammonViewSerializer
from .permissions import IsEditor


class BackgammonViewSet(viewsets.ModelViewSet):
    queryset = Backgammon.objects.all()
    serializer_class = BackgammonViewSerializer
    permission_classes = (IsEditor, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'tournament__name')


class BackgammonList(generics.ListAPIView):
    queryset = Backgammon.objects.all()
    serializer_class = BackgammonSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'tournament__name')



# class WeekDays(generics.ListAPIView):
#     week_day = self.kwargs['page']
#
#     if week_day==2:
#         queryset = Backgammon.objects.filter(week_day=week_day)
