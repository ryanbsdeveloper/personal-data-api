import sqlalchemy as sql
from . import database

class DataPersonal(database.Base):
    __tablename__ = "DadosPessoais"
    extend_existing=True

    id = sql.Column(sql.Integer, index=True, primary_key=True)
    nome = sql.Column(sql.String, index=True)
    sobrenome = sql.Column(sql.String, index=True)
    nascimento = sql.Column(sql.String, index=True)
    cpf = sql.Column(sql.String, index=True)
    cnpj = sql.Column(sql.String, index=True)
    uf = sql.Column(sql.String, index=True)
    cidade = sql.Column(sql.String, index=True)
    bairro = sql.Column(sql.String, index=True)
    rua = sql.Column(sql.String, index=True)
    sexo = sql.Column(sql.String, index=True)
