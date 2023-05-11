from rest_framework import serializers
from sport_matches.models import *


class TeamSerializator(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class SportTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = SportType
        fields = '__all__'



class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = '__all__'

# это список api/v1/matches/list/
class MatchViewSerializer(serializers.ModelSerializer):
    sport_type = SportTypeSerializer()
    tournament = TournamentSerializer()
    team_one = TeamSerializator()
    team_two = TeamSerializator()
    gender = serializers.CharField(source='get_gender_display', read_only=True)
    date = serializers.DateField(format='%Y.%m.%d', default=None)
    time = serializers.TimeField(format='%H:%M')

    class Meta:
        model = Match
        fields = '__all__'

# для админки
class MatchSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source='get_gender_display', read_only=True)
    date = serializers.DateField(format='%Y.%m.%d', default=None)
    time = serializers.TimeField(format='%H:%M')


    class Meta:
        model = Match
        fields = '__all__'


