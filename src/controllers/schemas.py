import pydantic

class _BaseDados(pydantic.BaseModel):
    nome: str
    sobrenome: str
    nascimento: str
    cpf: str
    cnpj: str
    uf: str
    cidade: str
    bairro: str
    rua: str
    sexo: str

class Dados(_BaseDados):
    id: int
    
    class Config:
        orm_mode = True

class CreateDados(_BaseDados):
    pass