from typing import List, Optional

import strawberry

from fruit.query import FRUIT_LIST
from fruit.type import AddFruitInput, Fruit, UpdateFruitInput


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

    @strawberry.mutation
    def update_fruit(self, updated_fruit: UpdateFruitInput) -> List[Fruit]:
        """ Mutation to update an existing Fruit in the list. """
        if existing_fruits := [fruit for fruit in FRUIT_LIST if fruit.name == updated_fruit.name]:
            for fruit in existing_fruits:
                fruit.quantity = updated_fruit.quantity

            return existing_fruits

        raise Exception(f'Fruit with name `{updated_fruit.name}` not found.')
