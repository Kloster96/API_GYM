from .entidad import Entidad

class Clase(Entidad):
    @classmethod
    def from_dict(cls, dict_data: dict):
        return cls(
            dict_data["id"],
            dict_data["nombre"],
            dict_data["duracion"],
            dict_data["entrenador_id"]
        )

    def __init__(self, id: int, nombre: str, duracion: int, entrenador_id: int):
        super().__init__(id)
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre debe ser un texto no vacío")
        if not isinstance(duracion, int) or duracion <= 0:
            raise ValueError("La duración debe ser un número entero positivo")
        if not isinstance(entrenador_id, int) or entrenador_id < 0:
            raise ValueError("El ID del entrenador debe ser un número entero positivo")
        
        self.__nombre = nombre
        self.__duracion = duracion
        self.__entrenador_id = entrenador_id
    
    def to_dict(self):
        return {
            "id": self._id,
            "nombre": self.__nombre,
            "duracion": self.__duracion,
            "entrenador_id": self.__entrenador_id
        }
