from rest_framework.viewsets import ModelViewSet
from .models import Character, Episode, Location
from .serializers import LocationSerializer, EpisodeSerializer, CharacterSerializer


class CharacterViewset(ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class LocationViewset(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class EpisodeViewset(ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

