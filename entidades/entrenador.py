from .entidad import Entidad

class Entrenador(Entidad):
    @classmethod
    def from_dict(cls, dict_data: dict):
        return cls(
            dict_data["id"],
            dict_data["nombre"],
            dict_data["especialidad"],
            dict_data["email"]
        )

    def __init__(self, id: int, nombre: str, especialidad: str, email: str):
        super().__init__(id)
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre debe ser un texto no vacío")
        if not isinstance(especialidad, str) or not especialidad.strip():
            raise ValueError("La especialidad debe ser un texto no vacío")
        if not isinstance(email, str) or not email.strip():
            raise ValueError("El email debe ser un texto no vacío")
        
        self.__nombre = nombre
        self.__especialidad = especialidad
        self.__email = email
    
    def to_dict(self):
        return {
            "id": self._id,
            "nombre": self.__nombre,
            "especialidad": self.__especialidad,
            "email": self.__email
        }
