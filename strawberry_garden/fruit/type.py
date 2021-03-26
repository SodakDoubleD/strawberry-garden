from typing import List

import strawberry


@strawberry.type
class Fruit:
    """ Fruit data structure definition for read queries. """
    name: str
    color: str
    quantity: int = 0


@strawberry.input
class AddFruitInput:
    """ Input definition for addFruit mutation. """
    name: str
    color: str
    quantity: int = 0


@strawberry.input
class UpdateFruitInput:
    """ Input definition for updateFruit mutation. """
    quantity: int


@strawberry.input
class RemoveFruitInput:
    """ Input definition for removeFruit mutation. """
    name: str
