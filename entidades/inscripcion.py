from .entidad import Entidad
from datetime import datetime

class Inscripcion(Entidad):
    @classmethod
    def from_dict(cls, dict_data: dict):
        return cls(
            dict_data["id"],
            dict_data["miembro_id"],
            dict_data["clase_id"],
            dict_data["fecha_inscripcion"]
        )

    def __init__(self, id: int, miembro_id: int, clase_id: int, fecha_inscripcion: str = None):
        super().__init__(id)
        if not isinstance(miembro_id, int) or miembro_id < 0:
            raise ValueError("El ID del miembro debe ser un número entero positivo")
        if not isinstance(clase_id, int) or clase_id < 0:
            raise ValueError("El ID de la clase debe ser un número entero positivo")
        
        self.__miembro_id = miembro_id
        self.__clase_id = clase_id
        self.__fecha_inscripcion = fecha_inscripcion or datetime.now().isoformat()
    
    def to_dict(self):
        return {
            "id": self._id,
            "miembro_id": self.__miembro_id,
            "clase_id": self.__clase_id,
            "fecha_inscripcion": self.__fecha_inscripcion
        }
