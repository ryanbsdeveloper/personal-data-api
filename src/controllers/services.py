from . import database
from . import models
from . import schemas

from sqlalchemy.orm import Session

def add_table():
    return database.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.session_local()
    
    try:
        yield db
    finally:
        db.close()

def get_all_datas(db: "Session") -> schemas.Dados:
    datas = db.query(models.DataPersonal).all()
    return list(map(schemas.Dados.from_orm, datas))