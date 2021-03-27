import strawberry

from fruit.mutation import FruitMutations
from fruit.query import FruitQueries
from garden.query import GardenQueries


@strawberry.type(description='Root query to house all other queries.')
class RootQuery(FruitQueries, GardenQueries):
    """ Root GraphQL query. """


@strawberry.type(description='Root mutation to house all other mutations.')
class RootMutation(FruitMutations):
    """ Root GraphQL mutation. """


schema = strawberry.Schema(query=RootQuery, mutation=RootMutation)
