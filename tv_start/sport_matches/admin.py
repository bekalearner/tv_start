from django.contrib import admin
from django.utils.safestring import mark_safe
from sport_matches.models import *


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('sport_type', 'tournament', 'team_one', 'team_two',
                    'get_image', 'created_date', 'match_date', 'time')
    readonly_fields = ('get_image', )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"/>')

    get_image.short_description = "Изображение"


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo', 'country')


@admin.register(Tournament)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('sport_type', 'name', 'gender')


admin.site.register(SportType)
