from typing import List, Optional

import strawberry

from fruit.type import Fruit


FRUIT_LIST = [
    Fruit(name='strawberry', color='red', quantity=10),
    Fruit(name='blueberry', color='blue', quantity=20),
    Fruit(name='kiwi', color='green', quantity=6),
]


@strawberry.type
class FruitQueries:
    """ Query definitions for Fruit objects. """

    @strawberry.field
    def fruits(self) -> List[Fruit]:
        """ Query to return all Fruit objects. """
        return FRUIT_LIST

    @strawberry.field
    def fruit(self, name: str) -> Optional[Fruit]:
        """ Query to return Fruit object based on name. """
        return next(iter(list(filter(lambda x: x.name == name, FRUIT_LIST))), None)
