import graphene

from .types import (
    PlayerType,
    PlayerBoardType
)
from .models import (
    Player,
    PlayerBoard
)
from .mutations import (
    CreateUserAndPlayerMutation,
    EditPlayerMottoMutation,
    DeleteUserAndPlayerMutation
)


class Query(graphene.ObjectType):
    players = graphene.List(PlayerType)
    player = graphene.Field(PlayerType, player_id=graphene.ID(required=True))
    player_board = graphene.List(PlayerBoardType)

    def resolve_players(self, info, **kwargs):
        return Player.objects.all()

    def resolve_player(self, info, player_id):
        return Player.objects.get(pk=player_id)

    def resolve_player_board(self, info, **kwargs):
        return PlayerBoard.objects.all()


class Mutation(graphene.ObjectType):
    create_user_and_player = CreateUserAndPlayerMutation.Field()
    update_player_motto = EditPlayerMottoMutation.Field()
    delete_user_and_player = DeleteUserAndPlayerMutation.Field()


schema = graphene.Schema(
    query=Query,
    mutation=Mutation
)
