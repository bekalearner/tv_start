from .models import Services
from rest_framework import generics
from .serializers import ServicesSerializer


class ServicesView(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer