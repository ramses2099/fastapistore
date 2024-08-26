import strawberry
from schema import SuperStoreType, SuperStoreInputType
from service.superstoreservice import SuperStoreService

@strawberry.type
class Mutation:

    @strawberry.mutation
    async def create_superstore(self, superstore_data: SuperStoreInputType) -> SuperStoreType:
        return await SuperStoreService.add_superstore(superstore_data)


    @strawberry.mutation
    async def delete_superstore(self, rowid: int) -> str:
        return await SuperStoreService.delete_superstore(rowid)


    @strawberry.mutation
    async def update_supersotre(self, rowid: int, superstore_data: SuperStoreInputType)->str:
        return await SuperStoreService.update_supertore(rowid, superstore_data)


