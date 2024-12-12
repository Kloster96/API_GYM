from .repositorio import Repositorio
from entidades.entrenador import Entrenador

class RepositorioEntrenadores(Repositorio):
    def __init__(self):
        super().__init__("datos/entrenadores.json")
    
    def _crear_entidad(self, datos: dict) -> Entrenador:
        return Entrenador.from_dict(datos)
