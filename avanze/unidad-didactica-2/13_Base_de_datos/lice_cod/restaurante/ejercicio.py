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
)# pedidos(plato_id,mesa_id, cantidad, fecha)
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




conn.execute(
    """
    INSERT INTO PLATOS (nombre,precio,categoria)
    VALUES ('Pizza', 10, 'italiana')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre,precio,categoria)
    VALUES ('Hamburguesa', 8, 'americana')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre,precio,categoria)
    VALUES ('sushi', 17.99, 'japonesa')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre,precio,categoria)
    VALUES ('ensalada', 6.99, 'vegetariana')
    """
)

conn.execute(
    """
    INSERT INTO MESAS (numero)
    VALUES (1)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero)
    VALUES (2)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero)
    VALUES (3)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero)
    VALUES (4)
    """
)

conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id,mesa_id, cantidad, fecha)
    VALUES (1,2,2,'2024-04-01')
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id,mesa_id, cantidad, fecha)
    VALUES (2,3,1,'2024-04-01')
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id,mesa_id, cantidad, fecha)
    VALUES (3,1,3,'2024-04-02')
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id,mesa_id, cantidad, fecha)
    VALUES (4,4,1,'2024-04-02')
    """
)


conn.execute(
    """
    UPDATE PLATOS
    SET precio = 9.99
    WHERE id = 2
    """
)

conn.execute(
    """
    UPDATE PLATOS
    SET categoria = 'Fusion'
    WHERE id = 3
    """
)

conn.execute(
    """
    DELETE FROM PEDIDOS
    where id = 3
    """
)

conn.commit()




conn.close()