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


# print("\Lista los empleados y sus salarios:")
# cursor = conn.execute(
#     """
#         SELECT salario,nombres,apellido_paterno,apellido_materno 
#         FROM SALARIOS 
#         INNER JOIN EMPLEADOS ON empleado_id=EMPLEADOS.id
  
#     """
# )
# for row in cursor:
#     print(row)

print("\Lista los empleados, el departamento en el que trabajan y el cargo que ocupan:")
cursor = conn.execute(
    """
        SELECT e.nombres, e.apellido_paterno, e.apellido_materno, d.nombre AS departamento, c.nombre AS cargo
        FROM EMPLEADOS AS e
        INNER JOIN CARGOS AS c ON e.codigo_id=c.id
        INNER JOIN DEPARTAMENTOS AS d ON e.departamento_id = d.id  
    """
)
for row in cursor:
    print(row)

print("Lista los empleados, el departamento en el que trabajan y el cargo que ocupan y el salario que ganan")
conn.execute(
    """
    SELECT e.nombres, e.apellido_paterno, e.apellido_materno, d.nombre AS departamento, c.nombre AS cargo, s.salario AS salario
    FROM SALARIOS AS s
    INNER JOIN EMPLEADOS AS e ON s.empleado_id=e.id
    INNER JOIN CARGOS AS c ON e.codigo_id=c.id
    INNER JOIN DEPARTAMENTOS AS d ON e.departamento_id = d.id
    """
)
print("UPDATE")
conn.execute(
    """
    UPDATE EMPLEADOS
    SET codigo_id = 1
    WHERE id = 2
    """
)
conn.commit()

conn.execute(
    """
    UPDATE SALARIOS
    SET salario = 3000
    WHERE id = 2
    """
)
conn.commit()

conn.execute(
    """
    DELETE FROM SALARIOS 
    WHERE id = 2;
    DELETE FROM EMPLEADOS
    WHERE id = 2;
    """
)
conn.commit()



# final parte
conn.execute(
    """
    INSERT INTO SALARIOS(empleado_id,salario,fecha_inicio,fecha_fin,fecha_creacion)
    VALUES (2,3500,'05-05-2023','05-05-2023','05-012-2024');
    INSERT INTO EMPLEADOS(nombres,apellido_paterno,apellido_materno,fecha_contratacion,departamento_id,codigo_id,fecha_creacion)
    VALUES ('carlos','rodriguez','sanchez','15-05-2023',1,3,'09-04-2024');
    """
)
conn.commit()


print("Lista los empleados, el departamento en el que trabajan y el cargo que ocupan y el salario que ganan")
conn.execute(
    """
    SELECT e.nombres, e.apellido_paterno, e.apellido_materno, d.nombre AS departamento, c.nombre AS cargo, s.salario AS salario
    FROM SALARIOS AS s
    INNER JOIN EMPLEADOS AS e ON s.empleado_id=e.id
    INNER JOIN CARGOS AS c ON e.codigo_id=c.id
    INNER JOIN DEPARTAMENTOS AS d ON e.departamento_id = d.id
    """
)

# cerrar conexion
conn.close()