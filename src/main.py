from typing import Any, Dict, List, Union
import fastapi
import sqlalchemy.orm as orm
from enum import Enum



from controllers import schemas
from controllers import services

tags_metadata = [
    {
        "name": "Pessoas",
        "description": "**Dados pessoais verídicos de pessoas fictícias.**",
    },
    {
        "name": "Autorização",
        "description": "**Consulte ou Crie seu HASH de autorização.**",
    }
]

app = fastapi.FastAPI(
    debug=True, version="0.0.1.0", title='Pessoas fictícias',
    contact={
        'name': 'Desenvolvedor',
        'email': 'ryanbsdeveloper@gmail.com'},
    openapi_tags=tags_metadata,
    docs_url='/',
    swagger_ui_parameters={"defaultModelsExpandDepth": -1}

)


class Sexualidade(str, Enum):
    Masculino = 'Masculino'
    Feminino = 'Feminino'


@app.get('/api/dados/', response_model=List[schemas.Dados], tags=["Pessoas"])
def consultar_dados_pessoais(db: orm.Session = fastapi.Depends(services.get_db),hash: str = fastapi.Query(description='**Informe seu HASH para autorização**', alias='Hash'),sexo: Sexualidade = fastapi.Query(None, alias='Sexualidade', description='Escolha entre **Masculino** e **Feminino**')):
    """
    **Dados de 200 pessoas.**
    """
    return services.get_all_datas(db=db, sexo=sexo, hash=hash)


@app.post('/api/auth/criar', response_model=schemas.Auth, tags=["Autorização"])
def criar_hash(db: orm.Session = fastapi.Depends(services.get_db), email: str = None):
    """
    **Codificação**: HASH MD5
    """

    return services.set_auth(db=db, email=email)

@app.get('/api/auth/consultar', response_model=schemas.Hash, tags=["Autorização"])
def consultar_hash(db: orm.Session = fastapi.Depends(services.get_db), email: str = fastapi.Query(description='Informe um email já cadastrado para realizar a consulta do HASH.')):

    return services.get_auth(db=db, email=email)