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
    gender = serializers.CharField(source='get_gender_display')
    class Meta:
        model = Tournament
        fields = '__all__'



class MatchSerializer(serializers.ModelSerializer):
    sport_type = SportTypeSerializer()
    tournament = TournamentSerializer()
    team_one = TeamSerializator()
    team_two = TeamSerializator()
    date = serializers.DateField(format='%Y.%m.%d', default=None)
    time = serializers.TimeField(format='%H:%M')
    def create(self, validated_data):
        # Если дата не указана в запросе, то устанавливаем ее по умолчанию
        if validated_data.get('date') is None:
            validated_data['date'] = self.instance.date
        return super().create(validated_data)


    class Meta:
        model = Match
        fields = '__all__'
