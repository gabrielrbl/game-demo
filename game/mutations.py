import graphene

from .types import GameType
from .models import Game


class CreateGameMutation(graphene.Mutation):
    class Arguments:
        date = graphene.Date(required=True)

    ok = graphene.Boolean()
    game = graphene.Field(GameType)

    def mutate(root, info, date):
        game = Game.objects.create(date=date)
        ok = True
        return CreateGameMutation(game=game, ok=ok)


class EditGamePlayersMutation(graphene.Mutation):
    class Arguments:
        game_id = graphene.ID(required=True)
        players_id = graphene.List(graphene.ID, required=True)

    ok = graphene.Boolean()
    game = graphene.Field(GameType)

    def mutate(root, info, game_id, players_id):
        game = Game.objects.get(pk=game_id)
        game.players.set(players_id)
        ok = True
        return CreateGameMutation(game=game, ok=ok)
