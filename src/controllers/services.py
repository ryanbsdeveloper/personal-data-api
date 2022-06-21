from enum import auto
from pyexpat import model
from attr import has
from pydantic import EmailError, EmailStr
import hashlib
from . import database
from . import models
from . import schemas

from sqlalchemy.orm import Session
from fastapi import HTTPException, Response


def add_table():
    return database.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.session_local()

    try:
        yield db
    finally:
        db.close()


def get_all_datas(db: "Session", sexo, hash) -> schemas.Dados:
    auth = db.query(models.AuthUsers).filter(models.AuthUsers.hash == hash)
    if auth.first():
        if sexo:
            if sexo.value == 'Masculino':
                datas = db.query(models.DataPersonal).filter(
                    models.DataPersonal.sexo == 'Masculino')
            elif sexo.value == 'Feminino':
                datas = db.query(models.DataPersonal).filter(
                    models.DataPersonal.sexo == 'Feminino')
        else:
            datas = db.query(models.DataPersonal).all()

        return list(map(schemas.Dados.from_orm, datas))

    raise HTTPException(status_code=401, detail='HASH inválido.')

def set_auth(db: "Session", email: EmailStr) -> schemas.Auth:
    if '@' not in str(email) or '.com' not in str(email):
        raise HTTPException(status_code=400, detail='E-mail inválido.')

    user = db.query(models.AuthUsers).filter(models.AuthUsers.email == email)
    if user.all():
        raise HTTPException(status_code=202, detail='E-mail já utilizado, consulte o HASH: api/auth/consultar ')

    md5 = hashlib.md5(email.encode())
    auth = models.AuthUsers(email=email, hash=md5.hexdigest())
    db.add(auth)
    db.commit()
    db.refresh(auth)
    
    return schemas.Auth.from_orm(auth)

def get_auth(db: "Session", email: EmailStr) -> schemas.Auth:
    user = db.query(models.AuthUsers).filter(models.AuthUsers.email == email)

    if user.first():
        hash = user.first().hash
        auth = models.AuthUsers(email=email, hash=hash)

        return schemas.Hash.from_orm(auth)

    raise HTTPException(status_code=404, detail='E-mail não cadastrado.')
