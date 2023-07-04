from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser

from tv_start.permissions import *
from .models import Article
from .serializers import ArticleSerializer
from datetime import datetime, timedelta


class ArticleList(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = Article.objects.filter(post_date__isnull=False).order_by('id', )
        # queryset = Article.objects.filter(post_date__isnull=False).order_by('post_date', 'time')

        q_value = self.request.GET.get('q')

        if q_value:
            try:
                q_value = int(q_value)
                queryset = queryset.filter(id__gt=q_value)
            except ValueError:
                pass

        # Получаем значение GET-параметра 'day_of_week'
        day_of_week = self.request.GET.get('day_of_week')

        # Если указан день недели, фильтруем новости по этому дню
        if day_of_week:
            # Получаем текущий день недели
            current_day_of_week = datetime.today().weekday()

            # Рассчитываем разницу дней для фильтрации
            days_difference = (int(day_of_week) - current_day_of_week) % 7

            # Рассчитываем дату для фильтрации
            current_date = datetime.now().date() + timedelta(days=days_difference)

            # Фильтруем новости по дню недели
            queryset = queryset.filter(post_date=current_date)

        return queryset


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-date', '-time')
    serializer_class = ArticleSerializer
    permission_classes = (Editor, )




