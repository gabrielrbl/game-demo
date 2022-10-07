import graphene

from .types import GameType
from .models import Game
from .mutations import (
    CreateGameMutation,
    EditGamePlayersMutation
)


class Query(graphene.ObjectType):
    games = graphene.List(GameType)

    def resolve_games(self, info, **kwargs):
        return Game.objects.all()


class Mutation(graphene.ObjectType):
    create_game = CreateGameMutation.Field()
    update_game_players = EditGamePlayersMutation.Field()


schema = graphene.Schema(
    query=Query,
    mutation=Mutation
)
