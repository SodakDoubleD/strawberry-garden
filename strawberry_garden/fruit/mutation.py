from typing import Optional

import strawberry

from fruit.query import FRUIT_LIST
from fruit.type import AddFruitInput, Fruit


@strawberry.type
class FruitMutations:
    """ Mutation definitions for Fruit objects. """

    @strawberry.mutation
    def add_fruit(self, new_fruit: AddFruitInput) -> Optional[Fruit]:
        """ Mutation to add a new Fruit to the list. """
        added_fruit = Fruit(
            name=new_fruit.name,
            color=new_fruit.color,
            quantity=new_fruit.quantity,
        )

        FRUIT_LIST.append(added_fruit)
        return added_fruit
