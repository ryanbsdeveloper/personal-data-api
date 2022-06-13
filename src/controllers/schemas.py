from decimal import Decimal
from typing import Optional
import pydantic
from datetime import date
from pydantic import EmailStr, constr

class Contato(pydantic.BaseModel):
    email: EmailStr
    telefone: str

class Cep(pydantic.BaseModel):
    cep: int
    uf: constr(max_length=2, strip_whitespace=False)
    cidade: str
    bairro: str
    rua: str

class Principal(pydantic.BaseModel):
    nome: str
    sobrenome: str
    nascimento: Optional[date]
    sexo: str
    cpf: str
    cnpj: str
    contato: Contato
    codigo_postal: Cep
    
class Dados(pydantic.BaseModel):
    id: int
    dados: Principal
    
    class Config:
        orm_mode = True

