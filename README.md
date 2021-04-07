# strawberry-garden
Python implementation of a GraphQL playground using the [strawberry library](https://github.com/strawberry-graphql/strawberry).


### Running the Basic Application With Pipenv
Pipenv has to be installed, that's a given.

In the root directory run:  
`pipenv install`

From the *strawberry_garden* directory run:  
`pipenv run uvicorn --reload main:app`

An interactive instance of GraphiQL can then be viewed at `http://localhost:8000/graphql`.
The `--reload` flag will cause uvicorn to automatically pick up any changes you make locally.
