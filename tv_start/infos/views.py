from rest_framework import generics
from .models import AllSiteInfo
from .serializers import InfoSerializer


class InfoView(generics.ListAPIView):
    queryset = AllSiteInfo.objects.all()
    serializer_class = InfoSerializer