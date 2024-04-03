# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("restaurante.db")

def mostrar():
    print("\platos:")
    cursor = conn.execute(
        "SELECT * FROM PLATOS"
    )
    for row in cursor:
        print(row)
    print("\mesas:")
    cursor = conn.execute(
        "SELECT * FROM MESAS"
    )
    for row in cursor:
        print(row)
    print("\pedidoss:")
    cursor = conn.execute(
        "SELECT * FROM PEDIDOS"
    )
    for row in cursor:
        print(row)

mostrar()
print()
def mostrar_JOIN():
    # Consultar datos de matriculación INNER JOIN
    print("\RSTAURANTE: INNER JOIN")
    cursor = conn.execute(
        """
        SELECT PLATOS.nombre, PLATOS.precio, PLATOS.categoria, MESAS.numero, PEDIDOS.cantidad, PEDIDOS.fecha
        FROM PEDIDOS
        JOIN PLATOS ON PEDIDOS.plato_id = PLATOS.id 
        JOIN MESAS ON PEDIDOS.mesa_id = MESAS.id
        
        """
    )
    for row in cursor:
        print(row)

def mostrar_LEFT_JOIN():
    # Consultar datos de matriculación INNER JOIN
    print("\RSTAURANTE: INNER JOIN")
    cursor = conn.execute(
        """
        SELECT PLATOS.nombre, PLATOS.precio, PLATOS.categoria, MESAS.numero, PEDIDOS.cantidad, PEDIDOS.fecha
        FROM PEDIDOS
        LEFT JOIN PLATOS ON PEDIDOS.plato_id = PLATOS.id 
        LEFT JOIN MESAS ON PEDIDOS.mesa_id = MESAS.id
        
        """
    )
    for row in cursor:
        print(row)

mostrar_JOIN()
mostrar_LEFT_JOIN()
conn.commit()
conn.close()