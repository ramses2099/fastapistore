from typing import Optional
from datetime import datetime
import strawberry

@strawberry.type
class SuperStoreType:
    rowid: int
    orderid: str
    orderdate: str
    shipdate: str
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


@strawberry.input
class SuperStoreInputType:
    orderid: str
    orderdate: str
    shipdate: str
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