
import uvicorn
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from strawberry.schema import Schema

from graphqlt.mutation import Mutation
from graphqlt.query import Query

from config import db


def init_app():
    apps = FastAPI(
        title="Fast API Store",
        description="Fast API",
        version="1.0.0"
    )

    async def startup():
        print('Start database table')
        await db.create_all()
    apps.add_event_handler("startup", startup)

    async def shutdown():
        await db.close()
    apps.add_event_handler("shutdown", shutdown)

    @apps.get('/')
    def index():
        return "Server is running"


    # schema
    schema = Schema(query=Query)
    graphql_app = GraphQLRouter(schema)

    apps.include_router(graphql_app, prefix='/graphql')

    return apps


app = init_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)

