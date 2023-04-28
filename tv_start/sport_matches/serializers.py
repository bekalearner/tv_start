from rest_framework import serializers
from sport_matches.models import *


class TeamSerializator(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('name', 'logo')


class SportTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportType
        fields = '__all__'


class TournamentSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source='get_gender_display')
    class Meta:
        model = Tournament
        fields = '__all__'



class MatchSerializer(serializers.ModelSerializer):
    sport_type = SportTypeSerializer()
    tournament = TournamentSerializer()
    team_one = TeamSerializator()
    team_two = TeamSerializator()
    date = serializers.DateField(format='%Y.%m.%d')
    time = serializers.TimeField(format='%H:%M')

    class Meta:
        model = Match
        fields = '__all__'