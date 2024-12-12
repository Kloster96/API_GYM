from abc import ABC, abstractmethod

class Entidad(ABC):
    def __init__(self, id: int):
        if not isinstance(id, int) or id < 0:
            raise ValueError("El ID debe ser un número entero positivo")
        self._id = id
    
    def obtener_id(self):
        return self._id