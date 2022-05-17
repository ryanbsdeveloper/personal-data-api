from flask_restplus import Resource

from src.models.model import DadosPessoaisModel
from src.models.serializer import DadosPessoaisSchema
from src.server.instancia import server

namespace = server.dados_ns

dados_serializer = DadosPessoaisSchema(many=True)

class DadosPessoais(Resource):

    @namespace.doc('Dados pessoais de pessoas fictícias')
    def get(self):
        dados = DadosPessoaisModel.find_all()
        return DadosPessoaisSchema.dump(dados), 200
