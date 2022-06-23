import sqlalchemy as sql
import sqlalchemy.ext.declarative as declarative
import sqlalchemy.orm as orm
import os

# POSTGRES DOCKER
#DATABASE_URL = f"postgresql://ryanl:password@db:5432/fastapi_database"

<<<<<<< HEAD
# POSTGRES HEROKU VARIÁVEL DE AMBIENTE
DATABASE_URL = os.environ['DATABASE_URL']
=======
# POSTGRES HEROKU
DATABASE_URL = f""
>>>>>>> 48c6ec08b3a5fa17796c1b58ece8263fca5ce917

engine = sql.create_engine(DATABASE_URL)

session_local = orm.sessionmaker(autocommit=False, autoflush=False,  bind=engine)

Base = declarative.declarative_base()
