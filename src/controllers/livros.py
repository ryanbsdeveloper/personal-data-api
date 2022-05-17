from flask import Flask
from flask_restplus import Api, Resource
from src.server.instancia import Server

app, api = Server.app, Server.api

livros = [
    {"id":0, "nome": "Harry Potter ea pedra filosofal"},
    {"id":1, "nome": "Harry Potter câmara secreta"},
    {"id":2, "nome": "Harry Potter eo prisioneiro de askaban"},
    {"id":3, "nome": "Harry Potter Cálice de fogo"},
]

api.route('/livros')
class Livros(Resource):
    def get(self):
        return(livros)
