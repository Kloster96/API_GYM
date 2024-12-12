from abc import ABC, abstractmethod
import json
from entidades.entidad import Entidad

class Repositorio(ABC):
    def __init__(self, archivo_json: str):
        self._archivo_json = archivo_json
        self._entidades = []  # Usamos una lista común
        self._cargar_entidades()
    
    def _cargar_entidades(self):
        try:
            with open(self._archivo_json, "r") as archivo:
                datos = json.load(archivo)
                self._entidades = [self._crear_entidad(item) for item in datos]
        except FileNotFoundError:
            print(f"No se encontró el archivo {self._archivo_json}")
            self._entidades = []
        except Exception as e:
            print(f"Error al cargar entidades: {str(e)}")
            self._entidades = []
    
    def _guardar_entidades(self):
        try:
            with open(self._archivo_json, "w") as archivo:
                json.dump([entidad.to_dict() for entidad in self._entidades], archivo, indent=4)
        except Exception as e:
            print(f"Error al guardar entidades: {str(e)}")
    
    @abstractmethod
    def _crear_entidad(self, datos: dict):
        pass
    
    def obtener_todos(self):
        return self._entidades
    
    def obtener_por_id(self, id: int):
        return next((e for e in self._entidades if e.obtener_id() == id), None)
    
    def agregar(self, entidad) -> None:
        if self.obtener_por_id(entidad.obtener_id()) is not None:
            raise ValueError(f"Ya existe una entidad con el ID {entidad.obtener_id()}")
        self._entidades.append(entidad)
        self._guardar_entidades()
    
    def actualizar(self, id: int, entidad) -> bool:
        for i, e in enumerate(self._entidades):
            if e.obtener_id() == id:
                self._entidades[i] = entidad
                self._guardar_entidades()
                return True
        return False
    
    def eliminar(self, id: int) -> bool:
        entidad = self.obtener_por_id(id)
        if entidad:
            self._entidades.remove(entidad)
            self._guardar_entidades()
            return True
        return False
