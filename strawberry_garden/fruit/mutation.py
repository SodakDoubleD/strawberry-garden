import strawberry

from type import AddFruitInput, Fruit


@strawberry.type
class AddFruitMutation:
    def add_fruit(self, input_val: AddFruitInput) -> Fruit:
        print(input_val)
