import strawberry

from strawberry_garden.fruit.mutation import FruitMutations
from strawberry_garden.fruit.query import FruitQueries
from strawberry_garden.garden.query import GardenQueries


@strawberry.type(description='Root query to house all other queries.')
class RootQuery(FruitQueries, GardenQueries):
    """ Root GraphQL query. """


@strawberry.type(description='Root mutation to house all other mutations.')
class RootMutation(FruitMutations):
    """ Root GraphQL mutation. """


schema = strawberry.Schema(query=RootQuery, mutation=RootMutation)
