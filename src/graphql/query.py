import strawberry

from schema import SuperStoreType
from service.superstoreservice import SuperStoreService

#TODO here
@strawberry.types
class Query:

    @strawberry.field
    def hello(self) -> str:
        return "hello hello"

    @strawberry.field
    async def get_all(self) -> list[SuperStoreType]:
        return await SuperStoreService.get_all_superstore()

    @strawberry.field
    async def get_by_id(self, id: int) -> SuperStoreType:
        return await SuperStoreService.get_by_id_superstore(id)
