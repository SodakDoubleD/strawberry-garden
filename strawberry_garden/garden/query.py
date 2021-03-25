from typing import List

import strawberry

from strawberry_garden.garden.type import Garden
from strawberry_garden.fruit.type import Fruit


def get_gardens():
    return [
        Garden(name='Harmony Park', fruits=[
            Fruit(name='strawberry', color='red', quantity=10),
            Fruit(name='blueberry', color='blue', quantity=20),
            Fruit(name='kiwi', color='green', quantity=6),
        ]),
        Garden(name='Paradise Place', fruits=[
            Fruit(name='pineapple', color='yellow', quantity=3),
            Fruit(name='raspberry', color='red', quantity=23),
        ]),
    ]


@strawberry.type
class GardenQueries:
    gardens: List[Garden] = strawberry.field(resolver=get_gardens)
