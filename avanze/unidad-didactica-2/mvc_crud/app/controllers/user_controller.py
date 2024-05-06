from flask import Blueprint, request, redirect, url_for
from datetime import datetime

from views import user_view
from models.user_model import User

user_bp = Blueprint("user", __name__)

@user_bp.route("/")
def usuarios():
    users = User.get_all()
    return user_view.usuarios(users)

@user_bp.route("/users", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form['email']
        contrasena = request.form['contrasena']
        fecha_nac = request.form['fecha_nac']
        user = User(first_name, last_name, email, contrasena, fecha_nac)
        user.save()
        return redirect(url_for("user.usuarios"))
    return user_view.registro()

@user_bp.route("/users/<int:id>", methods=["GET"])
def obtener_usuario(id):
    user = User.get_by_id(id)
    if not user:
        return "Usuario no encontrado", 404
    return user_view.actualizar(user)

@user_bp.route("/users/<int:id>", methods=["POST"])
def actualizar(id):
    user = User.get_by_id(id)
    if not user:
        return "Usuario no encontrado", 404
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    contrasena = request.form["contrasena"]
    fecha_nac = request.form["fecha_nac"]
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.contrasena = contrasena
    user.fecha_nac = datetime.strptime(fecha_nac, "%Y-%m-%d")
    user.update()
    return redirect(url_for("user.usuarios"))

# @user_bp.route("/users/<int:id>", methods=["DELETE"])
# def eliminar(id):
#     user = User.get_by_id(id)
#     if not user:
#         return "Usuario no encontrado", 404
#     user.delete()
#     return redirect(url_for("user.usuarios"))
@user_bp.route("/users/<int:id>", methods=["DELETE"])
def eliminar(id):
    user = User.get_by_id(id)
    if not user:
        return "Usuario no encontrado", 404
    user.delete()
    return redirect(url_for("user.usuarios"))

