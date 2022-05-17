from flask_restplus import Resource
from src.models.livro import BookModel
from src.models.serializer import BookSchema


livros_serializer = BookSchema(many=True)

class Livros(Resource):
    def get(self):
        livros = BookModel.find_all()
        return livros_serializer.dump(livros), 200
