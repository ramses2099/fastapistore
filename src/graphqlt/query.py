
import strawberry

from schema import SuperStoreType
from service.superstoreservice import SuperStoreService


@strawberry.type
class Query:

    @strawberry.field()
    def hello(self) -> str:
        return "hello hello"

    @strawberry.field
    async def get_all(self) -> list[SuperStoreType]:
        return await SuperStoreService.get_all_superstore()

    @strawberry.field
    async def get_by_id(self, rowid: int) -> SuperStoreType:
        return await SuperStoreService.get_by_id_superstore(rowid)
