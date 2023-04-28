from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser

from .models import Article
from .serializers import ArticleSerializer


class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAdminUser, )
