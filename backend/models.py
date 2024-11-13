"""
Archivo para definir los modelos de nuestra base de datos usando SQLAlquemy, que es un ORM muy popular en Python
Este modelo representa a la tabla en la base de datos
"""

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class ToDo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    completed = Column(Boolean, default=False)
