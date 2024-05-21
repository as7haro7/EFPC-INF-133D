# importamos la libreria para usar sql lite
import sqlite3

# creacion de la coneccion a la base de datos
conn=sqlite3.connect("instituto.db")

# creacion de tabla carreras
# en SQL litelos nombres de las tablas estan en mayuscula y plural
# y las variables estan en minusculas y en singular
try:
    conn.execute(
    """
    CREATE TABLE CARRERAS
    (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    duracion INTEGER NOT NULL   
    );
    """
    )


    # insercion de datos
    conn.execute(
        """
        INSERT INTO CARRERAS(nombre,duracion)
        VALUES('ingenieria en informatica', 5)
        """
    )
    conn.execute(
        """
        INSERT INTO CARRERAS(nombre,duracion)
        VALUES('licenciatura en administracion', 4)
        """
    )
except sqlite3.OperationalError:
    print("tabla carreras ya creada")

# consultar datos
print("carreras:")
cursor= conn.execute("SELECT * FROM CARRERAS")
for row in cursor:
    print(row)


try:
    # creacion de tabla estudiantes
    conn.execute(
        """
        CREATE TABLE ESTUDIANTES
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        fecha_nacimiento DATE NOT NULL    
        )
        """
    )

    # inseccion de datos en estudiantes
    conn.execute(
        """
        INSERT INTO ESTUDIANTES(nombre,apellido,fecha_nacimiento)
        VALUES('Juan','Perez','2000-05-15')
        """
    )
    conn.execute(
        """
        INSERT INTO ESTUDIANTES(nombre,apellido,fecha_nacimiento)
        VALUES('Elver','Galarga','2001-05-15')
        """
    )

    print("ESTUDIANTES:")
    cursor = conn.execute("SELECT * FROM ESTUDIANTES")
    for row in cursor:
        print(row)
except sqlite3.OperationalError:
    print("tabla estudiantes ya creada")


try:
    # creacion de tabla matriculacion
    conn.execute(
        """
        CREATE TABLE MATRICULACION
        (id INTEGER PRIMARY KEY,
        estudiante_id INTEGER NOT NULL,
        carrera_id INTEGER NOT NULL,
        fecha TEXT NOT NULL,
        FOREIGN KEY (estudiante_id) REFERENCES ESTUDIANTES(id),
        FOREIGN KEY (carrera_id) REFERENCES CARRERAS(id));
        """
    )

    # insertar datos ala tabla
    conn.execute(
    """
    INSERT INTO MATRICULACION (estudiante_id, carrera_id, fecha) 
    VALUES (1, 1, '2024-01-15')
    """
    )
    conn.execute(
        """
        INSERT INTO MATRICULACION (estudiante_id, carrera_id, fecha) 
        VALUES (2, 2, '2024-01-20')
        """
    )

    conn.execute(
        """
        INSERT INTO MATRICULACION (estudiante_id, carrera_id, fecha)
        VALUES (1, 2, '2024-01-25')
        """
    )
except sqlite3.OperationalError:
    print("tabla matriculacion ya creada")

# Consultar datos de matriculación
print("\nMATRICULACION:")
cursor = conn.execute(
    """
    SELECT ESTUDIANTES.nombre, ESTUDIANTES.apellido, CARRERAS.nombre, MATRICULACION.fecha 
    FROM MATRICULACION
    JOIN ESTUDIANTES ON MATRICULACION.estudiante_id = ESTUDIANTES.id 
    JOIN CARRERAS ON MATRICULACION.carrera_id = CARRERAS.id
    """
)
for row in cursor:
    print(row)

# Listar datos de matriculación
print("\nMATRICULACION:")
cursor = conn.execute(
    "SELECT * FROM MATRICULACION"
)

for row in cursor:
    print(row)

# actualizar una fila de la tablade matriculacion
conn.execute(
    """
    UPDATE MATRICULACION
    SET fecha = '2024-01-30'
    WHERE id = 2
    """
)


# para borrar
conn.execute(
    """
    DELETE FROM MATRICULACION
    WHERE id = 1
    """

)

# Listar datos de matriculación
print("\nMATRICULACION:")
cursor = conn.execute(
    "SELECT * FROM MATRICULACION"
)

for row in cursor:
    print(row)

# cerrar conexion
conn.close()