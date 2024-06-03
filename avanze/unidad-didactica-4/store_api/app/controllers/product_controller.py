from flask import Blueprint, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from models.product_model import Product
from views import product_view

# Importamos el decorador de roles
from utils.decorators import role_required

product_bp = Blueprint("product", __name__)


@product_bp.route("/products")
@login_required
def list_products():
    products = Product.get_all()
    return product_view.list_products(products)


@product_bp.route("/products/create", methods=["GET", "POST"])
@login_required
@role_required("admin")
def create_product():
    if request.method == "POST":
        if current_user.has_role("admin"):
            name = request.form["name"]
            description = request.form["description"]
            price = int(request.form["price"])
            stock = int(request.form["stock"])
            product = Product(name=name, description=description, price=price, stock=stock)
            product.save()
            flash("Producto creado exitosamente", "success")
            return redirect(url_for("product.list_products"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return product_view.create_product()


@product_bp.route("/products/<int:id>/update", methods=["GET", "POST"])
@login_required
@role_required("admin")
def update_product(id):
    product = Product.get_by_id(id)
    if not product:
        return "producto no encontrado", 404
    if request.method == "POST":
        if current_user.has_role("admin"):
            name = request.form["name"]
            description = request.form["description"]
            price = int(request.form["price"])
            stock = int(request.form["stock"])
            product.update(name=name, description=description, price=price, stock=stock)
            flash("product actualizado exitosamente", "success")
            return redirect(url_for("product.list_products"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return product_view.update_product(product)


@product_bp.route("/products/<int:id>/delete")
@login_required
@role_required("admin")
def delete_product(id):
    product = Product.get_by_id(id)
    if not product:
        return "product no encontrado", 404
    if current_user.has_role("admin"):
        product.delete()
        flash("product eliminado exitosamente", "success")
        return redirect(url_for("product.list_products"))
    else:
        return jsonify({"message": "Unauthorized"}), 403
