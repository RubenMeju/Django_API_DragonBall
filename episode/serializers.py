from rest_framework import serializers
from episode.models import Episode


class EpisodeSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = '__all__'
