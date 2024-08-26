from typing import Optional
from datetime import datetime
import strawberry

@strawberry.type
class SuperStoreType:
    rowid: int
    orderdate: datetime
    shipdate: datetime
    shipmode: str
    customerid: str


@strawberry.input
class SuperStoreInputType:
    orderid: str
    orderdate: datetime
    shipdate: datetime
    shipmode: str
    customerid: str
    customername: str
    segment: str
    country: str
    city: str
    state: str
    postalcode: str
    region: str
    productid: str
    category: str
    subcategory: str
    productname: str
    sales: float
    quantity: int
    discount: float
    profit: float