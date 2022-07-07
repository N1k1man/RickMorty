from rest_framework import serializers
from .models import Episode, Character, Location


class LocationSerializer(serializers.ModelSerializer):
    Location_birth = serializers.StringRelatedField(many=True, read_only=True)
    char_loc = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Location
        fields = ('id', 'title', 'izmerenie', 'desc', 'img', 'Location_birth', 'char_loc')


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ('id', 'title', 'numb_episode', 'desc', 'characters', 'img')


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('id', 'img', 'name', 'status', 'desc', 'race', 'gender', 'loc', 'birth_loc')