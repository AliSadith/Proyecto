import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchem.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

user = os.getenv("POSTGRESS_USER")
password = os.getenv("POSTGRESS_PASSSWORD")
database = os.getenv("POSTGRESS_DB")
host = os.getenv("POSTGRESS_HOST")
port = os.getenv("POSTGRESS_PORT")

SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

sessionlocal = sessionmarker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    print("obteniendo sesion de base de datos")
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()
        print("Sesion de base de datos cerrada")