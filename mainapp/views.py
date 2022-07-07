from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .models import Character, Episode, Location
from .serializers import LocationSerializer, EpisodeSerializer, CharacterSerializer


class CharacterViewset(ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [IsAuthenticatedOrReadOnly | IsAdminUser]


class LocationViewset(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly | IsAdminUser]


class EpisodeViewset(ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly | IsAdminUser]


