from starlette.applications import Starlette
from starlette.routing import Route
from strawberry.asgi import GraphQL

from schema import schema


routes = [
    Route('/graphql', endpoint=GraphQL(schema, graphiql=True))
]

app = Starlette(debug=True, routes=routes)
