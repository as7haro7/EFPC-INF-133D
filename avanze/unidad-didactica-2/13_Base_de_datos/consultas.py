# importamos la libreria para usar sql lite
import sqlite3

# creacion de la coneccion a la base de datos
conn=sqlite3.connect("instituto.db")


# Listar datos de matriculación
print("\nMATRICULACION:")
cursor = conn.execute(
    "SELECT * FROM CARRERAS"
)
for row in cursor:
    print(row)