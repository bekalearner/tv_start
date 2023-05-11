from rest_framework import serializers

from title.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    time = serializers.TimeField(format='%H:%M')
    class Meta:
        model = Article
        fields = '__all__'