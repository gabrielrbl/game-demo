from graphene_django import DjangoObjectType

from .models import Game


class GameType(DjangoObjectType):
    class Meta:
        model = Game
