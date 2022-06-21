from decimal import Decimal
from typing import Optional
import pydantic
from datetime import date
from pydantic import EmailStr
from sqlalchemy import ForeignKey, Sequence

class Contato(pydantic.BaseModel):
    email: EmailStr
    telefone: str

class Cep(pydantic.BaseModel):
    cep: int
    uf: str
    cidade: str
    bairro: str
    rua: str

class Dados(pydantic.BaseModel):
    nome: str
    sobrenome: str
    nascimento: str
    sexo: str
    cpf: str
    cnpj: str
    contato: Contato
    codigo_postal: Cep
        
    class Config:
        orm_mode = True
