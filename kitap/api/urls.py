from django.urls import path, include
from rest_framework.routers import DefaultRouter

from kitap.api.views import KitapViewSet

router = DefaultRouter()
router.register(r"kitap", KitapViewSet, basename="kitap")

urlpatterns = [
    path("", include(router.urls), name="kitap")
]
