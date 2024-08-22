from datetime import datetime
import strawberry

@strawberry.types
class SuperStoreType:
    rowid: int
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

@strawberry.types
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