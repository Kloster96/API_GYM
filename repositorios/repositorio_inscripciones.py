from .repositorio import Repositorio
from entidades.inscripcion import Inscripcion
from typing import List

class RepositorioInscripciones(Repositorio):
    def __init__(self):
        super().__init__("datos/inscripciones.json")
    
    def _crear_entidad(self, datos: dict) -> Inscripcion:
        return Inscripcion.from_dict(datos)
    
    def obtener_por_miembro(self, miembro_id: int) -> List[Inscripcion]:
        return [i for i in self._entidades if i.to_dict()["miembro_id"] == miembro_id]
    
    def obtener_por_clase(self, clase_id: int) -> List[Inscripcion]:
        return [i for i in self._entidades if i.to_dict()["clase_id"] == clase_id]
