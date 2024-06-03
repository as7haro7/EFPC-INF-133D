from flask import render_template
from flask_login import current_user


# La función `list_products` recibe una lista de
# animales y renderiza el template `animales.html`
def list_products(products):
    return render_template(
        "products.html",
        products=products,
        title="Lista de animales",
        current_user=current_user,
    )


# La función `create_product` renderiza el
# template `create_product.html` o devuelve un JSON
# según la solicitud
def create_product():
    return render_template(
        "create_product.html", title="Crear product", current_user=current_user
    )


# La función `update_product` recibe un product
# y renderiza el template `update_product.html`
def update_product(product):
    return render_template(
        "update_product.html",
        title="Editar product",
        product=product,
        current_user=current_user,
    )
