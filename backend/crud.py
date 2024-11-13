from sqlalchemy.orm import Session
import models, schemas


def create_todo(db: Session, todo: schemas.ToDoRequest):
    """
    Crea una nueva tarea en la base de datos.

    Args:
        db (Session): La sesión activa de la base de datos.
        todo (schemas.ToDoRequest): Un objeto de tipo ToDoRequest que contiene los datos de la tarea a crear.

    Returns:
        models.ToDo: El objeto ToDo creado con los datos persistidos, incluyendo cualquier campo generado automáticamente.
    """
    db_todo = models.ToDo(name=todo.name, completed=todo.completed)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def read_todos(db: Session, completed: bool):
    """
    Obtiene todas las tareas de la base de datos, con la opción de filtrar por estado de completado.

    Args:
        db (Session): La sesión activa de la base de datos.
        completed (bool): Un valor booleano para filtrar las tareas por su estado de completado.
                          Si es None, se devuelven todas las tareas.

    Returns:
        list[models.ToDo]: Una lista de objetos ToDo que representan las tareas en la base de datos.
    """
    if completed is None:
        return db.query(models.ToDo).all()
    else:
        return db.query(models.ToDo).filter(models.ToDo.completed == completed).all()


def read_todo(db: Session, id: int):
    """
    Obtiene una tarea específica de la base de datos por su ID.

    Args:
        db (Session): La sesión activa de la base de datos.
        id (int): El ID de la tarea que se desea obtener.

    Returns:
        models.ToDo: El objeto ToDo correspondiente al ID proporcionado, o None si no se encuentra.
    """
    return db.query(models.ToDo).filter(models.ToDo.id == id).first()


def update_todo(db: Session, id: int, todo: schemas.ToDoUpdate):
    """
    Actualiza una tarea existente en la base de datos.

    Args:
        db (Session): La sesión activa de la base de datos.
        id (int): El ID de la tarea que se desea actualizar.
        todo (schemas.ToDoRequest): Un objeto de tipo ToDoRequest con los nuevos datos de la tarea.

    Returns:
        models.ToDo: El objeto ToDo actualizado, o None si no se encuentra la tarea a actualizar.
    """
    db_todo = db.query(models.ToDo).filter(models.ToDo.id == id).first()
    if db_todo is None:
        return None

    db.query(models.ToDo).filter(models.ToDo.id == id).update(
        {"name": todo.name, "completed": todo.completed}
    )

    db.commit()
    db.refresh(db_todo)

    return db_todo


def delete_todo(db: Session, id: int):
    """
    Elimina una tarea de la base de datos por su ID.

    Args:
        db (Session): La sesión activa de la base de datos.
        id (int): El ID de la tarea que se desea eliminar.

    Returns:
        bool: True si la tarea fue eliminada exitosamente, o None si no se encuentra la tarea.
    """
    db_todo = db.query(models.ToDo).filter(models.ToDo.id == id).first()
    if db_todo is None:
        return None
    db.query(models.ToDo).filter(models.ToDo.id == id).delete()
    db.commit()

    return True
