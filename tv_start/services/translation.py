from modeltranslation.translator import register, TranslationOptions
from .models import Services


@register(Services)
class ServicesTranslationOption(TranslationOptions):
    fields = ('title', 'subtitle')