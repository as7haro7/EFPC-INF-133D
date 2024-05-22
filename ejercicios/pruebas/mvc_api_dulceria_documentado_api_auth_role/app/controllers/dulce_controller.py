from flask import Blueprint, request, jsonify
from models.dulce_model import Dulce
from views.dulce_view import render_dulce_detail, render_dulce_list
from utils.decorators import jwt_required, roles_required

dulce_bp = Blueprint("dulce", __name__)


# Ruta para obtener la lista de dulces
@dulce_bp.route("/dulces", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_dulces():
    dulces = Dulce.get_all()
    return jsonify(render_dulce_list(dulces))

# Ruta para obtener un dulce específico por su ID
@dulce_bp.route("/dulces/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_dulce(id):
    dulce = Dulce.get_by_id(id)
    if dulce:
        return jsonify(render_dulce_detail(dulce))
    return jsonify({"error": "dulce no encontrado"}), 404

# Ruta para crear un nuevo dulce
@dulce_bp.route("/dulces", methods=["POST"])
@jwt_required
# @roles_required(roles=["admin"])
def create_dulce():
    data = request.json
    marca = data.get("marca")
    peso_gramos = data.get("peso_gramos")
    fecha_elaboracion = data.get("fecha_elaboracion")
    con_azucar = data.get("con_azucar")
    sabor = data.get("sabor")
    origen = data.get("origen")

    # Validación simple de datos de entrada
    if not marca or not peso_gramos or not sabor or not origen:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    # Crear un nuevo dulce y guardarlo en la base de datos
    dulce = Dulce(
        marca=marca,
        peso_gramos=peso_gramos,
        fecha_elaboracion=fecha_elaboracion,
        con_azucar=con_azucar,
        sabor=sabor,
        origen=origen,
    )
    dulce.save()

    return jsonify(render_dulce_detail(dulce)), 201

# Ruta para actualizar un dulce existente
@dulce_bp.route("/dulces/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_dulce(id):
    dulce = Dulce.get_by_id(id)

    if not dulce:
        return jsonify({"error": "dulce no encontrado"}), 404

    data = request.json
    marca = data.get("marca")
    peso_gramos = data.get("peso_gramos")
    fecha_elaboracion = data.get("fecha_elaboracion")
    con_azucar = data.get("con_azucar")
    sabor = data.get("sabor")
    origen = data.get("origen")

    # Actualizar los datos del dulce
    dulce.update(
        marca=marca,
        peso_gramos=peso_gramos,
        fecha_elaboracion=fecha_elaboracion,
        con_azucar=con_azucar,
        sabor=sabor,
        origen=origen,
    )

    return jsonify(render_dulce_detail(dulce))

# Ruta para eliminar un dulce existente
@dulce_bp.route("/dulces/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_dulce(id):
    dulce = Dulce.get_by_id(id)

    if not dulce:
        return jsonify({"error": "dulce no encontrado"}), 404

    # Eliminar el dulce de la base de datos
    dulce.delete()

    # Respuesta vacía con código de estado 204 (sin contenido)
    return "dulce eliminado", 204
