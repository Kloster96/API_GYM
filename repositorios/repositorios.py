from .repositorio_miembros import RepositorioMiembros
from .repositorio_entrenadores import RepositorioEntrenadores
from .repositorio_clases import RepositorioClases
from .repositorio_inscripciones import RepositorioInscripciones

# Definimos variables globales para los repositorios
_repo_miembros = None
_repo_entrenadores = None
_repo_clases = None
_repo_inscripciones = None

# Función para obtener el repositorio de miembros
def obtener_repo_miembros():
    global _repo_miembros
    if _repo_miembros is None:
        _repo_miembros = RepositorioMiembros()
    return _repo_miembros

# Función para obtener el repositorio de entrenadores
def obtener_repo_entrenadores():
    global _repo_entrenadores
    if _repo_entrenadores is None:
        _repo_entrenadores = RepositorioEntrenadores()
    return _repo_entrenadores

# Función para obtener el repositorio de clases
def obtener_repo_clases():
    global _repo_clases
    if _repo_clases is None:
        _repo_clases = RepositorioClases()
    return _repo_clases

# Función para obtener el repositorio de inscripciones
def obtener_repo_inscripciones():
    global _repo_inscripciones
    if _repo_inscripciones is None:
        _repo_inscripciones = RepositorioInscripciones()
    return _repo_inscripciones
