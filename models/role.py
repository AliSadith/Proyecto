from sqlalchemy import Boolean, Column, Integer, String
from app.database import Base
from sqlalchmey.orm import relationship



class Role(Base):
    __tablename__ = "role"
    id=Column(integer, primary_key=True, idex=True)
    nombre = Column(String(200), idex=True)

    