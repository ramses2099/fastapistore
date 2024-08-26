from model.superstore import SuperStore
from repository.superstorerepository import SuperStoreRepository
from schema import SuperStoreInputType, SuperStoreType


class SuperStoreService:
    @staticmethod
    def superstore_superstoretype(superstore: SuperStore) -> SuperStoreType:
        print(superstore)
        superstoreType = SuperStoreType(rowid = superstore.rowid,
        orderid = superstore.orderid,
        orderdate = superstore.orderdate,
        shipdate = superstore.shipdate,
        shipmode = superstore.shipmode,
        customerid = superstore.customerid,
        customername = superstore.customername,
        segment = superstore.segment,
        country = superstore.country,
        city = superstore.city,
        state = superstore.state,
        postalcode = superstore.postalcode,
        region = superstore.region,
        productid = superstore.productid,
        category = superstore.category,
        subcategory = superstore.subcategory,
        productname = superstore.productname,
        sales = superstore.sales,
        quantity = superstore.quantity,
        discount = superstore.discount,
        profit = superstore.profit)
        return superstoreType

    @staticmethod
    async def add_superstore(superstore_data: SuperStoreInputType) -> SuperStoreType:
        superstore = SuperStore()
        superstore.orderid = superstore_data.orderid
        superstore.orderdate = superstore_data.orderdate
        superstore.shipdate = superstore_data.shipdate
        superstore.shipmode = superstore_data.shipmode
        superstore.customerid = superstore_data.customerid
        superstore.customername = superstore_data.customername
        superstore.segment = superstore_data.segment
        superstore.country = superstore_data.country
        superstore.city = superstore_data.city
        superstore.state = superstore_data.state
        superstore.postalcode = superstore_data.postalcode
        superstore.region = superstore_data.region
        superstore.productid = superstore_data.productid
        superstore.category = superstore_data.category
        superstore.subcategory = superstore_data.subcategory
        superstore.productname = superstore_data.productname
        superstore.sales = superstore_data.sales
        superstore.quantity = superstore_data.quantity
        superstore.discount = superstore_data.discount
        superstore.profit = superstore_data.profit
        await SuperStoreRepository.create(superstore)

        superstoretype = SuperStoreService.superstore_superstoretype(superstore)

        return superstoretype

    # TODO here working in the service layer for send back the data
    @staticmethod
    async def get_all_superstore() -> list[SuperStoreType]:
        list_superstore = await SuperStoreRepository.get_all()
        list_of_sup =[s[0] for s in list_superstore]
        return list_of_sup

    @staticmethod
    async def get_by_id_superstore(rowid: int) -> SuperStoreType:
        superstore = await SuperStoreRepository.get_by_id(rowid)
        return SuperStoreService.superstore_superstoretype(superstore)

    @staticmethod
    async def delete_superstore(rowid: int) -> str:
        await SuperStoreRepository.delete(rowid)
        return f'Successfully deleted data by id {rowid}'

    @staticmethod
    async def update_supertore(rowid: int, superstore_data: SuperStoreInputType) -> str:
        superstore = SuperStore()
        superstore.orderid = superstore_data.orderid
        superstore.orderdate = superstore_data.orderdate
        superstore.shipdate = superstore_data.shipdate
        superstore.shipmode = superstore_data.shipmode
        superstore.customerid = superstore_data.customerid
        superstore.customername = superstore_data.customername
        superstore.segment = superstore_data.segment
        superstore.country = superstore_data.country
        superstore.city = superstore_data.city
        superstore.state = superstore_data.state
        superstore.postalcode = superstore_data.postalcode
        superstore.region = superstore_data.region
        superstore.productid = superstore_data.productid
        superstore.category = superstore_data.category
        superstore.subcategory = superstore_data.subcategory
        superstore.productname = superstore_data.productname
        superstore.sales = superstore_data.sales
        superstore.quantity = superstore_data.quantity
        superstore.discount = superstore_data.discount
        superstore.profit = superstore_data.profit
        await  SuperStoreRepository.update(rowid, superstore)

        return f'Successfully updated data by id {rowid}'