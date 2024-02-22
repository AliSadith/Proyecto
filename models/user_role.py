from sqlalchemy import Colum, Integer, Foreignkey
from app.database import Base


class UserRole(Base):
    __tablename__ = 'user_role'
    user_id = Column(Integer, Foreignkey('user.id'), primary_key=True)
    role_id = Column(Integer, Foreignkey('role_id'), primary_key=True)
    