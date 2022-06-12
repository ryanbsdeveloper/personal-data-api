from typing import List
import fastapi
import sqlalchemy.orm as orm
from sqlalchemy.orm.base import PASSIVE_NO_FETCH_RELATED

from controllers import models, schemas
from controllers import services


app = fastapi.FastAPI(debug=True)

@app.post('/api/dados/', response_model=schemas.Dados)
def create_data(data: schemas.CreateDados, db: orm.Session = fastapi.Depends(services.get_db)):
    return services.create_data(data=data, db=db)


@app.get('/api/dados/', response_model=List[schemas.Dados])
def get_data(db: orm.Session = fastapi.Depends(services.get_db)):
    return services.get_all_datas(db=db)