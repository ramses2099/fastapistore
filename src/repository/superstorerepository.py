from multiprocessing.sharedctypes import synchronized

from sqlalchemy.sql import select
from sqlalchemy import update as sql_update, delete as sql_delete

from model.superstore import SuperStore
from config import db


class SuperStoreRepository:

    @staticmethod
    async def create(superstore: SuperStore):
        async with db as session:
            async with session.begin():
                session.add(superstore)
            await db.commit_rollback()

    @staticmethod
    async def get_by_id(rowid: int):
        async with db as session:
            stmt = select(SuperStore).where(SuperStore.rowid == rowid)
            result = await session.execute(stmt)
            superstore = result.first()
            return superstore

    @staticmethod
    async def get_last_rowid():
        async with db as session:
            stmt = select(SuperStore).order_by(SuperStore.rowid.desc()).limit(1)
            result = await session.execute(stmt)
            superstore = result.first()
            return superstore

    @staticmethod
    async def get_all(limit: int, offset: int):
        async with db as session:
            stmt = select(SuperStore).limit(limit).offset(offset)
            result = await session.execute(stmt)
            return result.all()

    @staticmethod
    async def update(self, rowid: int, sstore: SuperStore):
        async with db as session:
            stmt = select(SuperStore).where(SuperStore.rowid == rowid)
            result = await session.execute(stmt)
            superstore = result.first()

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