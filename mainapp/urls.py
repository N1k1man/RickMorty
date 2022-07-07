from rest_framework.routers import DefaultRouter
from .views import LocationViewset, CharacterViewset, EpisodeViewset

router = DefaultRouter()
router.register('location', LocationViewset)
router.register('character', CharacterViewset)
router.register('episode', EpisodeViewset)

urlpatterns = router.urls


