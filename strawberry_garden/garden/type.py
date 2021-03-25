from typing import List

import strawberry

from strawberry_garden.fruit.type import Fruit


@strawberry.type
class Garden:
    """ Garden data structure definition for read queries. """
    name: str
    fruits: List[Fruit]


@strawberry.type
class AddGardenInput:
    """ Input definition for addGarden mutation. """
    name: str
    fruits: List[Fruit]


@strawberry.type
class UpdateGardenInput:
    """ Input definition for updateGarden mutation. """
    fruits: List[Fruit]


@strawberry.type
class RemoveGardenInput:
    """ Input definition for removeGarden mutation. """
    name: str
