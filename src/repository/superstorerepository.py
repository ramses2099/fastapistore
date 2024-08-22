from multiprocessing.sharedctypes import synchronized

from sqlalchemy.sql import select
from sqlalchemy import update as sql_update, delete as sql_delete

from model.superstore import SuperStore
from config import db


class SuperStoreRepository:

    @staticmethod
    async def create(self, superstore: SuperStore):
        async with db as session:
            session.add(superstore)
        await db.commit_rollback()

    @staticmethod
    async def get_by_id(self, rowid: int):
        async with db as session:
            stmt = select(SuperStore).where(SuperStore.rowid == rowid)
            result = await session.execute(stmt)
            superstore = result.scalar().first()
            return superstore

    @staticmethod
    async def get_all(self, rowid: int):
        async with db as session:
            stmt = select(SuperStore)
            result = await session.execute(stmt)
            superstores = result.scalar().all()
            return superstores

    @staticmethod
    async def update(self, rowid: int, sstore: SuperStore):
        async with db as session:
            stmt = select(SuperStore).where(SuperStore.rowid == rowid)
            result = await session.execute(stmt)
            superstore = result.scalar().first()

            superstore.orderid = sstore.orderid
            superstore.orderdate = sstore.orderdate
            superstore.shipdate = sstore.shipdate
            superstore.shipmode = sstore.shipmode
            superstore.customerid = sstore.customerid
            superstore.customername = sstore.customername
            superstore.segment = sstore.segment
            superstore.country = sstore.country
            superstore.city = sstore.city
            superstore.state = sstore.state
            superstore.postalcode = sstore.postalcode
            superstore.region = sstore.region
            superstore.productid = sstore.productid
            superstore.category = sstore.category
            superstore.subcategory = sstore.subcategory
            superstore.productname = sstore.productname
            superstore.sales = sstore.sales
            superstore.quantity = sstore.quantity
            superstore.discount = sstore.discount
            superstore.profit = sstore.profit

            query = sql_update(SuperStore).where(SuperStore.rowid == rowid).values(
                **superstore.dict()
            ).execution_options(synchronize_session="fetch")

            await session.execute(query)
            await db.commit_rollback()

    @staticmethod
    async def delete(self, rowid):
        async with db as session:
            query = sql_delete(SuperStore).where(SuperStore.rowid == rowid)
            await session.execute(query)
            await db.commit_rollback()