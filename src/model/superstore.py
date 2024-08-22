from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field


class SuperStore(SQLModel, table=True):
    __tablename__ = "superstore"
    rowid: Optional[int] = Field(default=None, primary_key=True)
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
