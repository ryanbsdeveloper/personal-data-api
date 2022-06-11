from flask import Flask, Blueprint
from flask_restplus import Api, Resource, fields


class Server():
    def __init__(self):
        self.app = Flask(__name__)
        # self.api = Api(self.app, version='0.1',
        #                title='Livros',
        #                description='Varios livros',
        #                doc='/docs')
    
        self.bluePrint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.bluePrint, title='Dados Pessoais de Pessoas Fictícias', version='0.1')
        self.app.register_blueprint(self.bluePrint)

        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sql3.db'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['PROPAGATE_EXCEPTIONS'] = True
        self.dados_ns = self.dados_ns()

    def dados_ns(self, ):
        return self.api.namespace(name='Dados', description='Dados fictícios', path='/')

    def run(self):
        self.app.run(
            debug=True
        )


server = Server()
