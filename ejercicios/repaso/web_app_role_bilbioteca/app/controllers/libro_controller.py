from flask import Blueprint, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from models.animal_model import Animal
from views import animal_view

# Importamos el decorador de roles
from utils.decorators import role_required

# Blueprint es plano del controlador
libro_bp = Blueprint("libro", __name__)


@libro_bp.route("/animals")
# logueo
@login_required
def list_animals():
    animals = Animal.get_all()
    return animal_view.list_animals(animals)


@libro_bp.route("/animals/create", methods=["GET", "POST"])
@login_required
# permiso de role
@role_required("admin")
def create_animal():
    # lo siguiebte esta de mas, borrar en caso de error
    if request.method == "POST":
        if current_user.has_role("admin"):
            name = request.form["name"]
            species = request.form["species"]
            age = int(request.form["age"])
            animal = Animal(name=name, species=species, age=age)
            animal.save()
            flash("Animal creado exitosamente", "success")
            return redirect(url_for("animal.list_animals"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return animal_view.create_animal()


@libro_bp.route("/animals/<int:id>/update", methods=["GET", "POST"])
# logueo
@login_required
# role
@role_required("admin")
def update_animal(id):
    animal = Animal.get_by_id(id)
    if not animal:
        return "Animal no encontrado", 404
    if request.method == "POST":
        if current_user.has_role("admin"):
            name = request.form["name"]
            species = request.form["species"]
            age = int(request.form["age"])
            animal.update(name=name, species=species, age=age)
            flash("Animal actualizado exitosamente", "success")
            return redirect(url_for("animal.list_animals"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return animal_view.update_animal(animal)


@libro_bp.route("/animals/<int:id>/delete")
@login_required
@role_required("admin")
def delete_animal(id):
    animal = Animal.get_by_id(id)
    if not animal:
        return "Animal no encontrado", 404
        # borrar el siguiente if  y else esta de mas
    if current_user.has_role("admin"):
        animal.delete()
        flash("Animal eliminado exitosamente", "success")
        return redirect(url_for("animal.list_animals"))
    else:
        return jsonify({"message": "Unauthorized"}), 403
