from model.superstore import SuperStore
from repository.superstorerepository import SuperStoreRepository
from schema import SuperStoreInputType, SuperStoreType
from datetime import datetime


class SuperStoreService:

    @staticmethod
    async def add_superstore(superstore_data: SuperStoreInputType) -> SuperStoreType:
        superstore = SuperStore()
        superstore.orderid = superstore_data.orderid
        superstore.orderdate = datetime.strptime(superstore_data.orderdate, '%Y-%m-%d')
        superstore.shipdate = datetime.strptime(superstore_data.shipdate, '%Y-%m-%d')
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
        # TODO resolve this error the table don't have identity field
        superstore.rowid = 9995 # this code is temp
        await SuperStoreRepository.create(superstore)
        return SuperStoreType(
            orderid=superstore_data.orderid,
            orderdate=superstore_data.orderdate,
            shipdate=superstore_data.shipdate,
            shipmode=superstore_data.shipmode,
            customerid=superstore_data.customerid,
            customername=superstore_data.customername,
            segment=superstore_data.segment,
            country=superstore_data.country,
            city=superstore_data.city,
            state=superstore_data.state,
            postalcode=superstore_data.postalcode,
            region=superstore_data.region,
            productid=superstore_data.productid,
            category=superstore_data.category,
            subcategory=superstore_data.subcategory,
            productname=superstore_data.productname,
            sales=superstore_data.sales,
            quantity=superstore_data.quantity,
            discount=superstore_data.discount,
            profit=superstore_data.profit,
            rowid=-1
        )

    @staticmethod
    async def get_all_superstore(limit: int, offset: int) -> list[SuperStoreType]:
        list_superstore = await SuperStoreRepository.get_all(limit, offset)
        list_of_sup = [s[0] for s in list_superstore]
        return list_of_sup

    @staticmethod
    async def get_last_superstore_rowid() -> int:
        rowid = await SuperStoreRepository.get_last_rowid()
        return rowid[0].rowid

    @staticmethod
    async def get_by_id_superstore(rowid: int) -> SuperStoreType:
        superstore = await SuperStoreRepository.get_by_id(rowid)
        return superstore[0]

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
