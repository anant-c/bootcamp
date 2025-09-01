from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID

from conf.db import Base

class User_Try(Base):
    __tablename__ = "user_try"

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    age = Column(Integer, nullable=False)
    