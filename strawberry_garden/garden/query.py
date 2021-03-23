from typing import List
import strawberry

from type import Garden


@strawberry.type
class Query:
    gardens: List[Garden]
