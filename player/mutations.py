import graphene

from graphene_file_upload.scalars import Upload

from .types import (
    PlayerType,
    UserType
)
from .models import (
    User,
    Player,
    PlayerBoard
)


class CreateUserAndPlayerMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        picture = Upload(required=True)
        gender = graphene.String(required=True)
        birthday = graphene.Date(required=True)
        motto = graphene.String(required=True)

    ok = graphene.Boolean()
    player = graphene.Field(PlayerType)

    def mutate(
        root, info, username, first_name, last_name,
        email, password, picture, gender, birthday, motto
    ):
        user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        player_board = PlayerBoard.objects.create(points=0)
        player = Player.objects.create(
            user=user,
            picture=picture,
            gender=gender,
            birthday=birthday,
            motto=motto,
            board=player_board
        )
        ok = True
        return CreateUserAndPlayerMutation(player=player, ok=ok)


class EditPlayerMottoMutation(graphene.Mutation):
    class Arguments:
        player_id = graphene.ID(required=True)
        motto = graphene.String()

    ok = graphene.Boolean()
    player = graphene.Field(PlayerType)

    def mutate(root, info, player_id, motto):
        player = Player.objects.get(pk=player_id)
        player.motto = motto
        player.save()
        ok = True
        return EditPlayerMottoMutation(player=player, ok=ok)


class DeleteUserAndPlayerMutation(graphene.Mutation):
    class Arguments:
        user_id = graphene.ID(required=True)

    ok = graphene.Boolean()
    user = graphene.Field(UserType)

    def mutate(root, info, user_id):
        user = User.objects.get(pk=user_id)
        player_board = PlayerBoard.objects.get(players__user=user)
        player_board.delete()
        user.delete()
        ok = True
        return DeleteUserAndPlayerMutation(ok=ok)
