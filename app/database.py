import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import MetaData

load_dotenv()

user = "postgress"
password = "testing"
database = "my_basedatos"
host = "localhost"
port = "5432"

print(port,host)

SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

metadata = MetaData()
Base = declarative_base(metadata=metadata)

def get_db():
    print("obteniendo sesion de base de datos")
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()
        print("Sesion de base de datos cerrada")