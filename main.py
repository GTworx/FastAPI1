from fastapi import FastAPI
from typing import Optional
import schemas
import models
from fastapi import Depends
from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from database import engine, get_db

app = FastAPI()

# creates all tables defined in models module
models.Base.metadata.create_all(bind=engine)


@app.get("/about")
async def root():
    return {"message": "About: Hello World - from Centos App"}


@app.get("/customers/{id}")
async def get_customer(id: str):
    return {"data": f"Customer id : {id}"}

customers = [{"name": "Ahmet TOSUN", "gender": "Male"},
             {"name": "Tülay ŞAHİN", "gender": "Female"}
             ]


@app.get("/customers")
def get_customers(limit: int, gender: str):
    customers_return = []
    for cust in customers[:limit]:
        if cust["gender"] == gender:
            customers_return.append(cust)
    return {"data 3": customers_return}


@app.get("/toplam/{num1}/{num2}")
async def calc_toplam(num1: int, num2: int):
    return {"data": f"Toplam : {num1} + {num2} = {num1 + num2}"}

# Create Customer


@app.post("/customers",  status_code=status.HTTP_201_CREATED)
async def create_customer(request: schemas.Customer, db: Session = Depends(get_db)):
    new_customer = models.Customer(
        CustomerID=request.CustomerID,
        Gender=request.Gender,
        Age=request.Age,
        AnnualIncome=request.AnnualIncome,
        SpendingScore=request.SpendingScore
    )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer
