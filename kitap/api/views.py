from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet

from kitap.api.serializer import KitapSerializer
from kitap.models import Kitap


class KitapViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.UpdateModelMixin,
                   GenericViewSet):
    serializer_class = KitapSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Kitap.objects.all()
