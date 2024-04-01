# importamos la libreria para usar sql lite
import sqlite3

# creacion de la coneccion a la base de datos
conn=sqlite3.connect("instituto.db")


# consultar datos
print("\nMATRICULACION:")
cursor = conn.execute(
    "SELECT * FROM MATRICULACION"
)

for row in cursor:
    print(row)