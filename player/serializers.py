from rest_framework.serializers import ModelSerializer

from player.models import Player


class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"
