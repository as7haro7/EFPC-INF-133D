def render_dulce_list(dulces):
    return [
        {
            "id": dulce.id,
            "marca": dulce.marca,
            "peso_gramos": dulce.peso_gramos,  # Use "peso_gramos" instead of "peso"
            "fecha_elaboracion": dulce.fecha_elaboracion.strftime("%Y-%m-%d"),  # Format date
            "con_azucar": dulce.con_azucar,
            "sabor": dulce.sabor,
            "origen": dulce.origen,
        }
        for dulce in dulces
    ]

def render_dulce_detail(dulce):
    return {
        "id": dulce.id,
        "marca": dulce.marca,
        "peso_gramos": dulce.peso_gramos,
        "fecha_elaboracion": dulce.fecha_elaboracion.strftime("%Y-%m-%d"),
        "con_azucar": dulce.con_azucar,
        "sabor": dulce.sabor,
        "origen": dulce.origen,
    }
