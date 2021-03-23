from typing import List
import strawberry

from type import Fruit


@strawberry.type
class Query:
    fruits: List[Fruit]
