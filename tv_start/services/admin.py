from django.contrib import admin
from .models import Services
from modeltranslation.admin import TranslationAdmin


@admin.register(Services)
class ServicesAdmin(TranslationAdmin):
    list_display = ('subtitle_ru', 'title_ru')

# admin.site.register(Services)
