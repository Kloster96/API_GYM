from flask import Blueprint, jsonify, request
from repositorios.repositorios import obtener_repo_miembros, obtener_repo_inscripciones
from entidades.miembro import Miembro

bp_miembros = Blueprint("miembros", __name__)
repo_miembros = obtener_repo_miembros()
repo_inscripciones = obtener_repo_inscripciones()

@bp_miembros.route("/miembros", methods=["GET"])
def listar_miembros():
    try:
        miembros = [miembro.to_dict() for miembro in repo_miembros.obtener_todos()]
        return jsonify(miembros)
    except Exception as e:
        return jsonify({"error": "Error al obtener los miembros", "mensaje": str(e)}), 500

@bp_miembros.route("/miembros/<int:id>", methods=["GET"])
def obtener_miembro(id):
    miembro = repo_miembros.obtener_por_id(id)
    if miembro is None:
        return jsonify({"error": "Miembro no encontrado"}), 404
    return jsonify(miembro.to_dict())

@bp_miembros.route("/miembros/<int:id>/clases", methods=["GET"])
def obtener_clases_miembro(id):
    miembro = repo_miembros.obtener_por_id(id)
    if miembro is None:
        return jsonify({"error": "Miembro no encontrado"}), 404
    
    inscripciones = repo_inscripciones.obtener_por_miembro(id)
    return jsonify([inscripcion.to_dict() for inscripcion in inscripciones])

@bp_miembros.route("/miembros", methods=["POST"])
def crear_miembro():
    datos = request.json
    try:
        miembro = Miembro.from_dict(datos)
        repo_miembros.agregar(miembro)
        return jsonify({"mensaje": "Miembro creado con éxito", "miembro": miembro.to_dict()}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except KeyError as e:
        return jsonify({"error": f"Faltó el campo: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": "Error al crear el miembro", "mensaje": str(e)}), 500

@bp_miembros.route("/miembros/<int:id>", methods=["PUT"])
def actualizar_miembro(id):
    datos = request.json
    try:
        miembro = Miembro.from_dict(datos)
        if repo_miembros.actualizar(id, miembro):
            return jsonify({"mensaje": "Miembro actualizado con éxito", "miembro": miembro.to_dict()})
        return jsonify({"error": "Miembro no encontrado"}), 404
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except KeyError as e:
        return jsonify({"error": f"Faltó el campo: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": "Error al actualizar el miembro", "mensaje": str(e)}), 500

@bp_miembros.route("/miembros/<int:id>", methods=["DELETE"])
def eliminar_miembro(id):
    if repo_miembros.eliminar(id):
        return jsonify({"mensaje": "Miembro eliminado con éxito"})
    return jsonify({"error": "Miembro no encontrado"}), 404
