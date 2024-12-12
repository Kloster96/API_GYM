from .repositorio import Repositorio
from entidades.miembro import Miembro

class RepositorioMiembros(Repositorio):
    def __init__(self):
        super().__init__("datos/miembros.json")
    
    def _crear_entidad(self, datos: dict) -> Miembro:
        return Miembro.from_dict(datos)
