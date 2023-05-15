from rest_framework import serializers
from .models import *


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = '__all__'


class SportTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportType
        fields = '__all__'


class BackgammonSerializer(serializers.ModelSerializer):
    sport_type = SportTypeSerializer()
    tournament = TournamentSerializer()
    
    class Meta:
        model = Backgammon
        fields = '__all__'


class BackgammonViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Backgammon
        fields = '__all__'