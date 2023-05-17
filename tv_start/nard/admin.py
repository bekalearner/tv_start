from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


@admin.register(Backgammon)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('tournament', 'name', 'get_image', 'match_date', 'time', 'created_date')
    list_editable = ['name', 'match_date', 'time']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="80" height="60"/>')

    get_image.short_description = "Изображение"


admin.site.register(Tournament)