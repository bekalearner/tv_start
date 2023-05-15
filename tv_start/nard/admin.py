from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


@admin.register(Backgammon)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date', 'match_date', 'time', 'get_image', 'tournament')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="80"/>')

    get_image.short_description = "Изображение"


@admin.register(SportType)
class BackgammoniconAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_image')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="60" height="50"/>')

    get_image.short_description = "Изображение"


admin.site.register(Tournament)
