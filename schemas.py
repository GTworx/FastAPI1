from typing import Optional
from pydantic import BaseModel


class Customer(BaseModel):
    CustomerID: int
    Gender: Optional[str] = None
    Age: Optional[int] = None
    AnnualIncome: Optional[float] = None
    SpendingScore: Optional[int] = None
