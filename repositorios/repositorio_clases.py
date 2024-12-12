from .repositorio import Repositorio
from entidades.clase import Clase

class RepositorioClases(Repositorio):
    def __init__(self):
        super().__init__("datos/clases.json")
    
    def _crear_entidad(self, datos: dict) -> Clase:
        return Clase.from_dict(datos)
