from src.server.instancia import server
from src.controllers.livros import Livros
from src.models.livro import db

api = server.api
app = server.app

@app.before_first_request
def create_tables():
    db.create_all()

server.api.add_resource(Livros, '/books/')
server.run()
