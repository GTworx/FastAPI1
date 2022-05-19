from typing import Optional
from pydantic import BaseModel, Field


class Customer(BaseModel):
    customerId: Optional[int] = None
    customerFName: str=Field(default=None, max_length=50)
    customerLName: str=Field(default=None, max_length=50)
    customerEmail: str=Field(default=None, max_length=50)
    customerPassword: str=Field(default=None, max_length=200)
    customerStreet: str=Field(default=None, max_length=50)
    customerCity: str=Field(default=None, max_length=50)
    customerState: str=Field(default=None, max_length=50)
    customerZipcode: str=Field(default=None, max_length=50)
