from src.server.instancia import server
from src.controllers.views import DadosPessoais
from src.models.model import db, ma

api = server.api
app = server.app


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(DadosPessoais, '/dados')

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    server.run()
