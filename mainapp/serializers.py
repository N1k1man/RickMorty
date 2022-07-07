from rest_framework import serializers
from .models import Episode, Character, Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'title', 'izmerenie', 'desc', 'img')


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ('id', 'title', 'numb_episode', 'desc', 'characters', 'img')


class CharacterSerializer(serializers.ModelSerializer):
    model = Character
    fields = ('id', 'img', 'title', 'numb_episode', 'desc', 'characters')