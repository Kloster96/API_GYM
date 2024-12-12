from .entidad import Entidad

class Miembro(Entidad):
    @classmethod
    def from_dict(cls, dict_data: dict):
        return cls(
            dict_data["id"],
            dict_data["nombre"],
            dict_data["apellido"],
            dict_data["fecha_nacimiento"],
            dict_data["plan"]
        )

    def __init__(self, id: int, nombre: str, apellido: str, fecha_nacimiento: str, plan: str):
        super().__init__(id)
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre debe ser un texto no vacío")
        if not isinstance(apellido, str) or not apellido.strip():
            raise ValueError("El apellido debe ser un texto no vacío")
        if not isinstance(fecha_nacimiento, str) or not fecha_nacimiento.strip():
            raise ValueError("La fecha de nacimiento debe ser un texto no vacío")
        if not isinstance(plan, str) or not plan.strip():
            raise ValueError("El plan debe ser un texto no vacío")
        
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_nacimiento = fecha_nacimiento
        self.__plan = plan
    
    def to_dict(self):
        return {
            "id": self._id,
            "nombre": self.__nombre,
            "apellido": self.__apellido,
            "fecha_nacimiento": self.__fecha_nacimiento,
            "plan": self.__plan
        }
