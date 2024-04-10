# importamos la libreria para usar sql lite
import sqlite3

# creacion de la coneccion a la base de datos
conn=sqlite3.connect("personal.db")


# --creacion de tablas--
# conn.execute(
#     """
#     CREATE TABLE DEPARTAMENTOS
#     (
#     id INTEGER PRIMARY KEY,  
#     nombre TEXT NOT NULL, 
#     fecha_creacion TEXT NOT NULL 
#     );
#     """
# )
# conn.execute(
#     """
#     CREATE TABLE CARGOS
#     (
#     id INTEGER PRIMARY KEY,
#     nombre TEXT NOT NULL, 
#     nivel TEXT NOT NULL, 
#     fecha_creacion TEXT NOT NULL 
#     );
#     """
# )
# conn.execute(
#     """
#     CREATE TABLE EMPLEADOS
#     (
#     id INTEGER PRIMARY KEY,
#     nombres TEXT NOT NULL,
#     apellido_paterno TEXT NOT NULL,   
#     apellido_materno TEXT NOT NULL,   
#     fecha_contratacion DATE NOT NULL,   
#     departamento_id INTEGER NOT NULL,   
#     codigo_id INTEGER NOT NULL,   
#     fecha_creacion DATE NOT NULL,
#     FOREIGN KEY (departamento_id) REFERENCES DEPARTAMENTOS(DEPARTAMENTOS),
#     FOREIGN KEY (codigo_id) REFERENCES CARGOS(CARGOS)   
#     );
#     """
# )

# conn.execute(
#     """
#     CREATE TABLE SALARIOS
#     (
#     id INTEGER PRIMARY KEY,
#     empleado_id INTEGER NOT NULL,
#     salario REAL NOT NULL,
#     fecha_inicio DATE NOT NULL,
#     fecha_fin DATE NOT NULL,
#     fecha_creacion TEXT NOT NULL,

#     FOREIGN KEY (empleado_id) REFERENCES CARGOS(EMPLEADOS)   
#     );
#     """
# )

# --insercion de datos--
# conn.execute(
#     """
#     INSERT INTO DEPARTAMENTOS (nombre,fecha_creacion)
#     VALUES ('ventas','10-04-2020')
#     """
# )
# conn.execute(
#     """
#     INSERT INTO DEPARTAMENTOS (nombre,fecha_creacion)
#     VALUES ('marqueting','11-04-2020')
#     """
# )

# conn.execute(
#     """
#     INSERT INTO CARGOS(nombre,nivel,fecha_creacion)
#     VALUES ('gerente de vetnas','senior','10-04-2020')
#     """
# )
# conn.execute(
#     """
#     INSERT INTO CARGOS(nombre,nivel,fecha_creacion)
#     VALUES ('analista de marqueting','junior','11-04-2020')
#     """
# )
# conn.execute(
#     """
#     INSERT INTO CARGOS(nombre,nivel,fecha_creacion)
#     VALUES ('representante de datos','junior','12-04-2020')
#     """
# )
# conn.commit()


# conn.execute(
#     """
#     INSERT INTO EMPLEADOS(nombres,apellido_paterno,apellido_materno,fecha_contratacion,departamento_id,codigo_id,fecha_creacion)
#     VALUES ('juan','gonzales','perez','15-05-2023',1,1,'10-04-2020')
#     """
# )
# conn.execute(
#     """
#     INSERT INTO EMPLEADOS(nombres,apellido_paterno,apellido_materno,fecha_contratacion,departamento_id,codigo_id,fecha_creacion)
#     VALUES ('maria','lopez','martinez','20-06-2023',2,2,'20-06-2020')
#     """
# )
# conn.commit()

# conn.execute(
#     """
#     INSERT INTO SALARIOS(empleado_id,salario,fecha_inicio,fecha_fin,fecha_creacion)
#     VALUES (1,3000,'01-04-2024','30-04-2025','01-04-2024')
#     """
# )
# conn.execute(
#     """
#     INSERT INTO SALARIOS(empleado_id,salario,fecha_inicio,fecha_fin,fecha_creacion)
#     VALUES (2,3500,'01-07-2024','30-04-2024','01-07-2024')
#     """
# )
# conn.commit()


print("\empleados y salarios:")
cursor = conn.execute(
    """
        SELECT SALARIOS.salario, EMPLEADOS.nombres
        FROM SALARIOS
        JOIN EMPLEADOS ON SALARIOS.empleado_id = SALARIOS.id       
    """
)
for row in cursor:
    print(row)

print("\empleados , departamento y cargo:")
cursor = conn.execute(
    """
        SELECT *
        FROM EMPLEADOS
        INNER JOIN DEPARTAMENTOS ON EMPLEADOS.departamento_id = EMPLEADOS.id  
        INNER JOIN CARGOS ON EMPLEADOS.codigo_id = EMPLEADOS.id       
    """
)
for row in cursor:
    print(row)

# update
conn.execute(
    """
    UPDATE EMPLEADOS
    SET codigo_id = 3
    WHERE id = 2;
    """
)
conn.commit()

# cerrar conexion
conn.close()