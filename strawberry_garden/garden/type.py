from typing import List
import strawberry


@strawberry.type
class Garden:
    name: str
    fruits: List['Fruit']


@strawberry.type
class AddGardenInput:
    """ Input definition for addGarden mutation. """
    name: str
    fruits: List['Fruit']


@strawberry.type
class UpdateGardenInput:
    """ Input definition for updateGarden mutation. """
    fruits: List['Fruit']


@strawberry.type
class RemoveGardenInput:
    """ Input definition for removeGarden mutation. """
    name: str
