from rest_framework import serializers

from kitap.models import Kitap


class KitapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitap
        fields = "__all__"
