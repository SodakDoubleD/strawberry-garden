import strawberry

from strawberry_garden.fruit.query import FruitQueries
from strawberry_garden.garden.query import GardenQueries


@strawberry.type(description='Root query to house all other queries.')
class RootQuery(FruitQueries, GardenQueries):
    """ Root GraphQL query. """


schema = strawberry.Schema(query=RootQuery)
