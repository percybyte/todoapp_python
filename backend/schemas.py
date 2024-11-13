"""
Definir el modelo de los datos: estructura, tipo, validaciones y configuraciones adicionales
"""

from pydantic import BaseModel
from typing import Optional


class ToDoRequest(BaseModel):
    name: str
    completed: bool


class ToDoResponse(BaseModel):
    name: str
    completed: bool
    id: int

    class Config:
        """
        Permitir que el modelo funcione con ORM como SQLAlchemy.
        Resulta útil cuando recuperamos datos de una base de datos mediante un ORM (mapeo relacional de objetos)
        y entregamos esos datos en un formato estructurado a través de una API.
        """

        orm_mode: True


class ToDoUpdate(BaseModel):
    name: Optional[str] = None
    completed: Optional[bool] = None
