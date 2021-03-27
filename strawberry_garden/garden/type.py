from dataclasses import field
from typing import List, Optional

import strawberry

from fruit.type import Fruit


@strawberry.type
class Garden:
    """ Garden data structure definition for read queries. """
    name: str
    fruits: List[Fruit] = field(default_factory=[])


@strawberry.type
class AddGardenInput:
    """ Input definition for addGarden mutation. """
    name: str
    fruits: Optional[List[Fruit]]


@strawberry.type
class UpdateGardenInput:
    """ Input definition for updateGarden mutation. """
    fruits: List[Fruit]


@strawberry.type
class RemoveGardenInput:
    """ Input definition for removeGarden mutation. """
    name: str
