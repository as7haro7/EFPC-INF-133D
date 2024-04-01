# base de datos para restaurante

# platos(nombre,precio,categoria)
# mesas(numero)
# pedidos(plato,mesa, cantidad, fecha)

# importamos la libreria para usar sql lite
import sqlite3

# creacion de la coneccion a la base de datos
conn=sqlite3.connect("restaurante.db")

conn.execute(
    """
    CREATE TABLE PLATOS
    (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio INTEGER NOT NULL,  
    categoria TEXT NOT NULL   
    );
    """
)
conn.execute(
    """
    CREATE TABLE MESAS
    (
    id INTEGER PRIMARY KEY,
    numero INTEGER NOT NULL    
    );
    """
)# pedidos(plato,mesa, cantidad, fecha)
conn.execute(
        """
        CREATE TABLE PEDIDOS
        (id INTEGER PRIMARY KEY,
        plato_id INTEGER NOT NULL,
        mesa_id INTEGER NOT NULL,
        cantidad INTEGER NOT NULL,
        fecha DATE NOT NULL,
        FOREIGN KEY (plato_id) REFERENCES PLATOS(id),
        FOREIGN KEY (mesa_id) REFERENCES MESAS(id));
        """
)

print("\platos:")
cursor = conn.execute(
    "SELECT * FROM PLATOS"
)
print("\mesas:")
cursor = conn.execute(
    "SELECT * FROM MESAS"
)
print("\pedidoss:")
cursor = conn.execute(
    "SELECT * FROM PEDIDOS"
)

