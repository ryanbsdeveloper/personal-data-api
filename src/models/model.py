from typing import List
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()

class DadosPessoaisModel(db.Model):
    __tablename__ = "Dados Pessoais"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False, unique=True)
    pages = db.Column(db.Float(precision=2), nullable=False)

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __repr__(self):
        return f'BookModel(title={self.title}, pages={self.pages})'

    def json(self):
        return {'title': self.title, 'pages': self.pages}

    @classmethod
    def find_by_title(cls, title) -> "DadosPessoaisModel":
        return cls.query.filter_by(title=title).first()

    @classmethod
    def find_by_id(cls, _id) -> "DadosPessoaisModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["DadosPessoaisModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

