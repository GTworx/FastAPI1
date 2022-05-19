from ast import Break
from bdb import Breakpoint
from fastapi import FastAPI
from fastapi import Depends
from fastapi import status, HTTPException
from sqlalchemy import VARCHAR
from sqlalchemy.orm import Session
from database2 import engine, get_db
import schemas2

import pandas as pd
import models2

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


# Creates all the tables defined in models module
models2.Base.metadata.create_all(bind=engine)

customer_raw = pd.read_csv("https://raw.githubusercontent.com/erkansirin78/datasets/master/retail_db/customers.csv")

customer_raw.to_sql('customers_raw', con=engine, index=False, if_exists='replace')

app = FastAPI()


@app.get("/about")
async def about():
    return {"message": "Hello World, uvicorn from virtual"}


# Get Customer by Id
@app.get("/customer/{id}", status_code=status.HTTP_200_OK)
async def get_customer_by_id(id: int, db: Session = Depends(get_db)):
    customer = db.query(models2.Customer).filter(models2.Customer.customerId == id).first()

    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Customer {id} has not found.")

    return customer


# Create 20 customers in one batch
@app.post("/batchinput", status_code=status.HTTP_201_CREATED)
async def create_customer_with_batch_input(db: Session = Depends(get_db)):
    counter = 1
    for custEntry in customer_raw.itertuples(index=False):
        if counter > 20:
            break

        # add below line if you do not want autoincrement
        # customerId = custEntry[customer_raw.columns.get_loc('customerId')],
        new_customer = models2.Customer(
            customerFName=custEntry[customer_raw.columns.get_loc('customerFName')],
            customerLName=custEntry[customer_raw.columns.get_loc('customerLName')],
            customerEmail=custEntry[customer_raw.columns.get_loc('customerEmail')],
            customerPassword=get_password_hash(custEntry[customer_raw.columns.get_loc('customerPassword')]),
            customerStreet=custEntry[customer_raw.columns.get_loc('customerStreet')],
            customerCity=custEntry[customer_raw.columns.get_loc('customerCity')],
            customerState=custEntry[customer_raw.columns.get_loc('customerState')],
            customerZipcode=custEntry[customer_raw.columns.get_loc('customerZipcode')]
        )

        db.add(new_customer)
        counter += 1

    db.commit()
    db.refresh(new_customer)

    return {"detail": f"Customers created."}


# Create Customer 2
@app.post("/createcustomer", status_code=status.HTTP_201_CREATED)
async def create_one_customer(request: schemas2.Customer, db: Session = Depends(get_db)):
    new_customer = models2.Customer(
        customerId=request.customerId,
        customerFName=request.customerFName,
        customerLName=request.customerLName,
        customerEmail=request.customerEmail,
        customerPassword=request.customerPassword,
        customerStreet=request.customerStreet,
        customerCity=request.customerCity,
        customerState=request.customerState,
        customerZipcode=request.customerZipcode
    )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer


# 8 id numaralı kayıtta Smith soyadını Fox olarak değiştiriniz.
@app.put("/customer/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_customer(id: int, db: Session = Depends(get_db)):
    customer = db.query(models2.Customer).filter(models2.Customer.customerId == id).first()

    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Customer {id} has not found.")

    customer.customerLName = 'Fox'

    db.commit()
    return {"detail": f"Customer {id} updated."}


# 4 id numaralı (Mary,Jones) kaydını siliniz.
# Delete a customer
@app.delete("/customer/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_customer(id: int, db: Session = Depends(get_db)):
    customer = db.query(models2.Customer).filter(models2.Customer.customerId == id).first()

    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Customer {id} has not found.")

    db.delete(customer)
    db.commit()

    return {"detail": f"Customer {id} deleted."}


# async def delete_customer2(id: int, db: Session = Depends(get_db)):
#  db.query(models.Customer).filter(models.Customer.customerId == id).delete(synchronize_session=False)
#  db.commit()
# return {"detail": f"Customer {id} deleted."}

# customerCity=Caguas olan kayıtlardan 3 tanesini seçiniz.
@app.get("/customer/{city}")
async def customer_by_city(city: str, db: Session = Depends(get_db)):
    customer = db.query(models2.Customer).filter(models2.Customer.customerCity == city).limit(3).all()

    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"There is no customer with {city} as city.")

    return customer
