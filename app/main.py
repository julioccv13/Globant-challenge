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
    # TODO: Podrias usar Pandas to sql, o iterar y hacer puros commit
    # TODO: Un ejemplo posible (aunque es mas eficiente el df.to_sql..)
    # with get_session() as (session, _):
    #         for d in tqdm(self.data_dict):
    #             d.update({"CurrentDate": current_date})
    #             t = RawFireIncidentsModel(**d)
    #             session.add(t)

    #         session.commit()
    pass

dump()