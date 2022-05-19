from database import Base
from sqlalchemy import Column, String, Integer, Float


class Customer(Base):
    __tablename__ = "customers"

    CustomerID = Column(Integer, primary_key=True)
    Gender = Column(String)
    Age = Column(Integer)
    AnnualIncome = Column(Float)
    SpendingScore = Column(Integer)