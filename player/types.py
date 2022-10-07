from graphene_django import DjangoObjectType
from django.contrib.auth.models import User

from .models import (
    Player,
    PlayerBoard
)


class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude = ('password',)


class PlayerType(DjangoObjectType):
    class Meta:
        model = Player


class PlayerBoardType(DjangoObjectType):
    class Meta:
        model = PlayerBoard
