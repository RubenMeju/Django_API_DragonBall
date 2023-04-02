from rest_framework import serializers
from character.models import Character
from planet.serializers import PlanetSerialzer


class CharacterSerializer(serializers.ModelSerializer):
    planet = PlanetSerialzer(many=False)

    class Meta:
        model = Character
        fields = '__all__'
