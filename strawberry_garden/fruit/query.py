from typing import List
import strawberry

from type import Fruit


def get_fruits():
    return [
        Fruit(name='strawberry', color='red', quantity=10),
        Fruit(name='blueberry', color='blue', quantity=20),
        Fruit(name='kiwi', color='green', quantity=6),
    ]


@strawberry.type
class Query:
    fruits: List[Fruit] = strawberry.field(resolver=get_fruits)
