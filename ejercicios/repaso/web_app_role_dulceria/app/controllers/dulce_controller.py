from flask import Blueprint, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from models.dulce_model import Dulce
from views import dulce_view

# Importamos el decorador de roles
from utils.decorators import role_required

# Blueprint es plano del controlador
dulce_bp = Blueprint("dulce", __name__)


@dulce_bp.route("/dulces")
# logueo
@login_required
def list_dulces():
    dulces = Dulces.get_all()
    return dulce_view.list_dulces(dulces)


@dulce_bp.route("/dulces/create", methods=["GET", "POST"])
@login_required
# permiso de role
@role_required("admin")
def create_dulce():
    # lo siguiebte esta de mas, borrar en caso de error
    if request.method == "POST":
        if current_user.has_role("admin"):
            marca = request.form["marca"]
            peso = request.form["peso"]
            sabor = int(request.form["sabor"])
            origen = int(request.form["origen"])
            dulce = Dulce(marca=marca, peso=peso, sabor=sabor, origen=origen)
            dulce.save()
            flash("Dulce creado exitosamente", "success")
            return redirect(url_for("dulce.list_dulce"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return dulce_view.create_dulce()


@dulce_bp.route("/dulces/<int:id>/update", methods=["GET", "POST"])
# logueo
@login_required
# role
@role_required("admin")
def update_animal(id):
    animal = Animal.get_by_id(id)
    if not animal:
        return "Dulce no encontrado", 404
    if request.method == "POST":
        if current_user.has_role("admin"):
            marca = request.form["marca"]
            peso = request.form["peso"]
            sabor = int(request.form["sabor"])
            origen = int(request.form["origen"])
            dulce = Dulce(marca=marca, peso=peso, sabor=sabor, origen=origen)
            flash("Dulce actualizado exitosamente", "success")
            return redirect(url_for("dulce.list_dulces"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return animal_view.update_animal(animal)


@dulce_bp.route("/dulces/<int:id>/delete")
@login_required
@role_required("admin")
def delete_dulce(id):
    dulce = Dulce.get_by_id(id)
    if not dulce:
        return "Dulce no encontrado", 404
        # borrar el siguiente if  y else esta de mas
    if current_user.has_role("admin"):
        dulce.delete()
        flash("dulce eliminado exitosamente", "success")
        return redirect(url_for("dulce.list_dulces"))
    else:
        return jsonify({"message": "Unauthorized"}), 403
