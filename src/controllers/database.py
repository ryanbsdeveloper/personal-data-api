import sqlalchemy as sql
import sqlalchemy.ext.declarative as declarative
import sqlalchemy.orm as orm


DATABASE_URL = f"postgresql://ryanl:password@localhost:5432/fastapi_database"

engine = sql.create_engine(DATABASE_URL)

session_local = orm.sessionmaker(autocommit=False, autoflush=False,  bind=engine)

Base = declarative.declarative_base()