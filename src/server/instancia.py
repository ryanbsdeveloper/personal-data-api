from flask import Flask
from flask_restplus import Api, Resource, fields
import ssl

class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app,
        version='0.1',
        title='Livros',
        description='Varios livros',
        doc='/docs')

        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sql3.db'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['PROPAGATE_EXCEPTIONS'] = True

    def run(self):
        self.app.run(
            debug=True
            )

server = Server()
