import graphene
import game.schema
import player.schema


class Query(
    game.schema.Query,
    player.schema.Query,
    graphene.ObjectType
):
    pass


class Mutation(
    game.schema.Mutation,
    player.schema.Mutation,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(
    query=Query,
    mutation=Mutation
)
