from django.contrib import admin
from .models import Article


@admin.register(Article)
class Article(admin.ModelAdmin):
    list_display = ['date', 'title', 'title_live', 'post_date', 'time', 'url']
    list_editable = ['title_live', 'title', 'post_date', 'time', 'url']
    ordering = ['date', 'post_date']
    list_per_page = 15
