from decimal import Decimal
from typing import Any, Hashable, Optional, Union
import pydantic
from datetime import date
from pydantic import EmailStr
from sqlalchemy import ForeignKey, Sequence


class Hash(pydantic.BaseModel):
    hash: str
    
    class Config:
        arbitrary_types_allowed = True
        orm_mode = True

class CriarAuth(pydantic.BaseModel):
    email: EmailStr

    class Config:
        orm_mode = True


class Auth(pydantic.BaseModel):
    email: EmailStr
    hash: str

    class Config:
        orm_mode = True


class Dados(pydantic.BaseModel):
    nome: str
    sobrenome: str
    nascimento: str
    sexo: str
    cpf: str
    cnpj: str
    email: EmailStr
    telefone: str
    cep: int
    uf: str
    cidade: str
    bairro: str
    rua: str

    class Config:
        orm_mode = True
