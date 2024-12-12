from flask import Blueprint, jsonify, request
from repositorios.repositorios import obtener_repo_inscripciones, obtener_repo_miembros, obtener_repo_clases
from entidades.inscripcion import Inscripcion

bp_inscripciones = Blueprint("inscripciones", __name__)
repo_inscripciones = obtener_repo_inscripciones()
repo_miembros = obtener_repo_miembros()
repo_clases = obtener_repo_clases()

@bp_inscripciones.route("/inscripciones", methods=["POST"])
def crear_inscripcion():
    datos = request.json

    # Verificar que los campos necesarios estén presentes
    campos_obligatorios = ["miembro_id", "clase_id", "fecha_inscripcion"]
    for campo in campos_obligatorios:
        if campo not in datos:
            return jsonify({"error": f"El campo '{campo}' es obligatorio"}), 400

    try:
        # Verificar que existen el miembro y la clase
        miembro = repo_miembros.obtener_por_id(datos["miembro_id"])
        if miembro is None:
            return jsonify({"error": "El miembro especificado no existe"}), 404
        
        clase = repo_clases.obtener_por_id(datos["clase_id"])
        if clase is None:
            return jsonify({"error": "La clase especificada no existe"}), 404
        
        # Crear la inscripción
        inscripcion = Inscripcion.from_dict(datos)
        repo_inscripciones.agregar(inscripcion)
        return jsonify({
            "mensaje": "Inscripción creada con éxito",
            "inscripcion": inscripcion.to_dict()
        }), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@bp_inscripciones.route("/inscripciones/<int:id>", methods=["DELETE"])
def eliminar_inscripcion(id):
    if repo_inscripciones.eliminar(id):
        return jsonify({"mensaje": "Inscripción eliminada con éxito"})
    return jsonify({"error": "Inscripción no encontrada"}), 404
