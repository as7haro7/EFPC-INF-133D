from flask import render_template
from flask_login import current_user


# La función `list_dulces` recibe una lista de
# animales y renderiza el template `animales.html`
def list_dulces(dulces):
    return render_template(
        "dulces.html",
        dulces=dulces,
        title="Lista de dulces",
        current_user=current_user,
    )


# La función `create_dulce` renderiza el
# template `create_dulce.html` o devuelve un JSON
# según la solicitud
def create_dulce():
    return render_template(
        "create_dulce.html", title="Crear dulce", current_user=current_user
    )


# La función `update_dulce` recibe un dulce
# y renderiza el template `update_dulce.html`
def update_dulce(dulce):
    return render_template(
        "update_dulce.html",
        title="Editar dulce",
        dulce=dulce,
        current_user=current_user,
    )
