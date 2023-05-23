import django_filters
from sport_matches.models import *
from django import forms
import calendar
import locale


# установка локали
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')


def get_years():
    """ Возвращает список годов с пустым полем """
    years = [(year, year) for year in range(2015, 2025)]
    years.insert(0, ('', '--------'))
    return years


def get_months():
    """ Возвращает список месяцев на русском языке с пустым полем """
    months = [(month, calendar.month_name[month]) for month in range(1, 13)]
    months.insert(0, ('', '--------'))
    return months


class MatchFilter(django_filters.FilterSet):
    sport_type = django_filters.ModelChoiceFilter(queryset=SportType.objects.all())
    tournament = django_filters.ModelChoiceFilter(queryset=Tournament.objects.all())
    year = django_filters.NumberFilter(field_name='match_date', lookup_expr='year',
                                       widget=forms.Select(choices=get_years()))
    month = django_filters.NumberFilter(field_name='match_date', lookup_expr='month',
                                        widget=forms.Select(choices=get_months()))

    class Meta:
        model = Match
        fields = ['year', 'month', 'sport_type']
