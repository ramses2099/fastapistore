
import strawberry

from schema import SuperStoreType
from service.superstoreservice import SuperStoreService


@strawberry.type
class Query:

    @strawberry.field
    async def get_all(self,limit: int, offset: int) -> list[SuperStoreType]:
        return await SuperStoreService.get_all_superstore(limit, offset)

    @strawberry.field
    async def get_by_id(self, rowid: int) -> SuperStoreType:
        return await SuperStoreService.get_by_id_superstore(rowid)

    @strawberry.field
    async def get_lat_rowid(self) -> int:
        return await SuperStoreService.get_last_superstore_rowid()