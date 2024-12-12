from flask import Blueprint, jsonify, request
from repositorios.repositorios import obtener_repo_entrenadores, obtener_repo_clases
from entidades.entrenador import Entrenador

bp_entrenadores = Blueprint("entrenadores", __name__)
repo_entrenadores = obtener_repo_entrenadores()
repo_clases = obtener_repo_clases()

@bp_entrenadores.route("/entrenadores", methods=["GET"])
def listar_entrenadores():
    return jsonify([entrenador.to_dict() for entrenador in repo_entrenadores.obtener_todos()])

@bp_entrenadores.route("/entrenadores/<int:id>", methods=["GET"])
def obtener_entrenador(id):
    entrenador = repo_entrenadores.obtener_por_id(id)
    if entrenador is None:
        return jsonify({"error": "Entrenador no encontrado"}), 404
    return jsonify(entrenador.to_dict())

@bp_entrenadores.route("/entrenadores/<int:id>/clases", methods=["GET"])
def obtener_clases_entrenador(id):
    entrenador = repo_entrenadores.obtener_por_id(id)
    if entrenador is None:
        return jsonify({"error": "Entrenador no encontrado"}), 404
    
    clases = [clase for clase in repo_clases.obtener_todos() 
             if clase.to_dict()["entrenador_id"] == id]
    return jsonify([clase.to_dict() for clase in clases])

@bp_entrenadores.route("/entrenadores", methods=["POST"])
def crear_entrenador():
    datos = request.json

    # Verificar si los campos obligatorios están presentes
    campos_obligatorios = ["nombre", "especialidad", "email"]
    for campo in campos_obligatorios:
        if campo not in datos:
            return jsonify({"error": f"El campo '{campo}' es obligatorio"}), 400

    try:
        entrenador = Entrenador.from_dict(datos)
        repo_entrenadores.agregar(entrenador)
        return jsonify({"mensaje": "Entrenador creado con éxito", "entrenador": entrenador.to_dict()}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@bp_entrenadores.route("/entrenadores/<int:id>", methods=["PUT"])
def actualizar_entrenador(id):
    datos = request.json
    try:
        entrenador = Entrenador.from_dict(datos)
        if repo_entrenadores.actualizar(id, entrenador):
            return jsonify({"mensaje": "Entrenador actualizado con éxito", "entrenador": entrenador.to_dict()})
        return jsonify({"error": "Entrenador no encontrado"}), 404
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@bp_entrenadores.route("/entrenadores/<int:id>", methods=["DELETE"])
def eliminar_entrenador(id):
    if repo_entrenadores.eliminar(id):
        return jsonify({"mensaje": "Entrenador eliminado con éxito"})
    return jsonify({"error": "Entrenador no encontrado"}), 404
