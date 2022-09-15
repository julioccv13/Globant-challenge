from fastapi import FastAPI
from typing import Union, List
import glob
import pandas as pd

from modules.models import Products
from modules.db import Session, get_session, create_engine


app = FastAPI()


@app.post("/create")
def create(product: Products):
    with get_session() as session:
        product = Products.from_orm(product)
        session.add(product)
        session.commit()
        session.refresh(product)


@app.post("/dump")
def dump():
    Session()
    engine = create_engine('postgresql://postgres:password@localhost:5433/db1')
    path = "./data"
    files = glob.glob(path + "/*.csv")

    for file in files:
        df1 = pd.read_csv(file) 
        df1.to_sql(file, con=engine, if_exists='append', index=False)
    pass
 

@app.post("/load")
def load():
   #pdx.to_avro()
    pass

dump()
