from rest_framework import serializers
from .models import *


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = '__all__'


class BackgammonSerializer(serializers.ModelSerializer):
    tournament = TournamentSerializer()
    
    class Meta:
        model = Backgammon
        fields = '__all__'


class BackgammonViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Backgammon
        fields = '__all__'