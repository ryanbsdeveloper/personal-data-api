from typing import List
import fastapi
import sqlalchemy.orm as orm
from sqlalchemy.orm.base import PASSIVE_NO_FETCH_RELATED

from controllers import models, schemas
from controllers import services

tags_metadata = [
    {
        "name": "Pessoas",
        "description": "**Dados pessoais verídicos de pessoas fictícias.**",
    },
]

app = fastapi.FastAPI(
        debug=True, version="0.0.1.0", title='Pessoas fictícias',
        contact={
        'name': 'Ryan',
        'url': 'https://port-ryansilva.herokuapp.com/',
        'email': 'ryanbsdeveloper@gmail.com'},
        openapi_tags=tags_metadata,
        docs_url='/api',
        redoc_url='/documentação'
        )


@app.get('/api/dados/', response_model=List[schemas.Dados], tags=["Pessoas"])
def get_data(db: orm.Session = fastapi.Depends(services.get_db)):
    return services.get_all_datas(db=db)