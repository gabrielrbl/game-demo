from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from player.serializers import PlayerSerializer
from player.models import Player


class PlayerViewSet(ModelViewSet):
    """ViewSet for the Player model."""
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    def get_queryset(self):
        queryset = self.queryset

        user = self.request.user

        if not user.is_staff:
            queryset = queryset.filter(user=user)

        return queryset
