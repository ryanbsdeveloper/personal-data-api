import sqlalchemy as sql
import sqlalchemy.ext.declarative as declarative
import sqlalchemy.orm as orm

# POSTGRES DOCKER
#DATABASE_URL = f"postgresql://ryanl:password@db:5432/fastapi_database"

# POSTGRES HEROKU
DATABASE_URL = f""

engine = sql.create_engine(DATABASE_URL)

session_local = orm.sessionmaker(autocommit=False, autoflush=False,  bind=engine)

Base = declarative.declarative_base()
