from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, CustomUserUpdateAPIView
from django.urls import path


router = DefaultRouter()
router.register('users', CustomUserViewSet)
urlpatterns = [
    path('change_user/<int:pk>', CustomUserUpdateAPIView.as_view())
]
urlpatterns += router.urls