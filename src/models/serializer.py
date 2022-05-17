from .model import ma
from .model import DadosPessoaisModel


class DadosPessoaisSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DadosPessoaisModel
        load_instance = True