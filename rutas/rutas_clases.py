from flask import Blueprint, jsonify, request
from repositorios.repositorios import obtener_repo_clases, obtener_repo_entrenadores, obtener_repo_inscripciones
from entidades.clase import Clase

bp_clases = Blueprint("clases", __name__)
repo_clases = obtener_repo_clases()
repo_entrenadores = obtener_repo_entrenadores()
repo_inscripciones = obtener_repo_inscripciones()

@bp_clases.route("/clases", methods=["GET"])
def listar_clases():
    return jsonify([clase.to_dict() for clase in repo_clases.obtener_todos()])

@bp_clases.route("/clases/<int:id>", methods=["GET"])
def obtener_clase(id):
    clase = repo_clases.obtener_por_id(id)
    if clase is None:
        return jsonify({"error": "Clase no encontrada"}), 404
    return jsonify(clase.to_dict())

@bp_clases.route("/clases/<int:id>/miembros", methods=["GET"])
def obtener_miembros_clase(id):
    clase = repo_clases.obtener_por_id(id)
    if clase is None:
        return jsonify({"error": "Clase no encontrada"}), 404
    
    inscripciones = repo_inscripciones.obtener_por_clase(id)
    return jsonify([inscripcion.to_dict() for inscripcion in inscripciones])

@bp_clases.route("/clases", methods=["POST"])
@bp_clases.route("/clases", methods=["POST"])
def crear_clase():
    datos = request.json
    required_fields = ["entrenador_id", "nombre", "duracion"]  # Asegúrate de que estos campos sean los requeridos

    # Verificar si faltan campos obligatorios
    for field in required_fields:
        if field not in datos:
            return jsonify({"error": f"El campo '{field}' es obligatorio"}), 400
    
    try:
        # Verificar que existe el entrenador
        entrenador = repo_entrenadores.obtener_por_id(datos["entrenador_id"])
        if entrenador is None:
            return jsonify({"error": "El entrenador especificado no existe"}), 404
        
        clase = Clase.from_dict(datos)
        repo_clases.agregar(clase)
        return jsonify({"mensaje": "Clase creada con éxito", "clase": clase.to_dict()}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@bp_clases.route("/clases/<int:id>", methods=["PUT"])
def actualizar_clase(id):
    datos = request.json
    try:
        # Verificar que existe el entrenador
        entrenador = repo_entrenadores.obtener_por_id(datos["entrenador_id"])
        if entrenador is None:
            return jsonify({"error": "El entrenador especificado no existe"}), 404
        
        clase = Clase.from_dict(datos)
        if repo_clases.actualizar(id, clase):
            return jsonify({"mensaje": "Clase actualizada con éxito", "clase": clase.to_dict()})
        return jsonify({"error": "Clase no encontrada"}), 404
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@bp_clases.route("/clases/<int:id>", methods=["DELETE"])
def eliminar_clase(id):
    if repo_clases.eliminar(id):
        return jsonify({"mensaje": "Clase eliminada con éxito"})
    return jsonify({"error": "Clase no encontrada"}), 404
