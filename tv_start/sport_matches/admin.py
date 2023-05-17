from django.contrib import admin
from django.utils.safestring import mark_safe
from sport_matches.models import *


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ['tournament', 'sport_type', 'team_one', 'team_two',
                    'get_image', 'created_date', 'match_date', 'time']
    list_editable = ['team_one', 'team_two', 'sport_type', 'match_date', 'time']
    readonly_fields = ('get_image', )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="80" height="60"/>')

    get_image.short_description = "Изображение"


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_image', 'country']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.logo.url} width="80" height="60"/>')

    get_image.short_description = "Изображение"

@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ['sport_type', 'name', 'gender']
    list_editable = ['name', 'gender']


@admin.register(SportType)
class SportAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_image']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.logo.url} width="30" height="30"/>')

    get_image.short_description = "Изображение"