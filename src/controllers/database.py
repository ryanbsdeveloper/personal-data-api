import sqlalchemy as sql
import sqlalchemy.ext.declarative as declarative
import sqlalchemy.orm as orm


DATABASE_URL = f"postgres://wtrsiuspjnorvg:707f69c0ec822ee5e4e5a2a84151d5adaee9672af69e357aac33cfe54cead93b@ec2-23-23-182-238.compute-1.amazonaws.com:5432/d9jr2mvsnnnsd1"

engine = sql.create_engine(DATABASE_URL)

session_local = orm.sessionmaker(autocommit=False, autoflush=False,  bind=engine)

Base = declarative.declarative_base()