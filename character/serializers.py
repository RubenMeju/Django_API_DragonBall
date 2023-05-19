from rest_framework import serializers
from character.models import Character


class CharacterSerializer(serializers.ModelSerializer):
    species = serializers.CharField(source='get_species_display')
    gender = serializers.CharField(source='get_gender_display')

    class Meta:
        model = Character
        fields = '__all__'
