from rest_framework import serializers
from .models import AllSiteInfo


class InfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = AllSiteInfo
        fields = '__all__'