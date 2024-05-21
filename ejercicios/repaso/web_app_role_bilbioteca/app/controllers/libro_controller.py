from flask import Blueprint, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from models.libro_model import Libro
from views import libro_view

# Importamos el decorador de roles
from utils.decorators import role_required

# Blueprint es plano del controlador
libro_bp = Blueprint("libro", __name__)


@libro_bp.route("/libros")
# logueo
@login_required
def list_libros():
    libros = Libro.get_all()
    return libro_view.list_libros(libros)


@libro_bp.route("/libros/create", methods=["GET", "POST"])
@login_required
# permiso de role
@role_required("admin")
def create_libro():
    # lo siguiebte esta de mas, borrar en caso de error
    if request.method == "POST":
        if current_user.has_role("admin"):
            autor = request.form["autor"]
            edicion = request.form["edicion"]
            disponibilidad = int(request.form["disponibilidad"])
            animal = Libro(autor=autor, edicion=edicion, disponibilidad=disponibilidad)
            animal.save()
            flash("Libro creado exitosamente", "success")
            return redirect(url_for("libro.list_libros"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return libro_view.create_libro()


@libro_bp.route("/libros/<int:id>/update", methods=["GET", "POST"])
# logueo
@login_required
# role
@role_required("admin")
def update_libro(id):
    libro = Libro.get_by_id(id)
    if not libro:
        return "libro no encontrado", 404
    if request.method == "POST":
        if current_user.has_role("admin"):
            autor = request.form["autor"]
            edicion = request.form["edicion"]
            disponibilidad = int(request.form["disponibilidad"])
            libro.update(autor=autor, edicion=edicion, disponibilidad=disponibilidad)
            flash("Libro actualizado exitosamente", "success")
            return redirect(url_for("libro.list_libros"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return libro_view.update_libro(libro)


@libro_bp.route("/libros/<int:id>/delete")
@login_required
@role_required("admin")
def delete_libro(id):
    libro = Libro.get_by_id(id)
    if not libro:
        return "libro no encontrado", 404
        # borrar el siguiente if  y else esta de mas
    if current_user.has_role("admin"):
        libro.delete()
        flash("libro eliminado exitosamente", "success")
        return redirect(url_for("libro.list_libros"))
    else:
        return jsonify({"message": "Unauthorized"}), 403
