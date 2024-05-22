from datetime import datetime
from database import db


# Define la clase `Dulce` que hereda de `db.Model`
# `Dulce` representa la tabla `Dulces` en la base de datos
class Dulce(db.Model):
    __tablename__ = "dulces"

    # Define las columnas de la tabla `dulces`
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(100), nullable=False)

    # Fecha de elaboracion (date)
    fecha_elaboracion = db.Column(db.Date, nullable=False)

    # Peso en gramos (float)
    peso_gramos = db.Column(db.Float, nullable=False)

    # Indica si tiene azucar (boolean)
    con_azucar = db.Column(db.Boolean, nullable=False)

    # Sabor (String)
    sabor = db.Column(db.String(100), nullable=False)

    # Origen (String)
    origen = db.Column(db.String(100), nullable=False)

    # Inicializa la clase `dulce`
    def __init__(self, marca, fecha_elaboracion, peso_gramos, con_azucar, sabor, origen):
        self.marca = marca
        self.fecha_elaboracion = fecha_elaboracion
        self.peso_gramos = peso_gramos
        self.con_azucar = con_azucar
        self.sabor = sabor
        self.origen = origen

    # Guarda un dulce en la base de datos
    def save(self):
        # Convierte la fecha_elaboracion a datetime
        if isinstance(self.fecha_elaboracion, str):
            fecha_elaboracion_datetime = datetime.strptime(self.fecha_elaboracion, "%Y-%m-%d")
            self.fecha_elaboracion = fecha_elaboracion_datetime

        # Guarda el dulce en la base de datos
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los dulcees de la base de datos
    @staticmethod
    def get_all():
        return Dulce.query.all()

    # Obtiene un dulce por su ID
    @staticmethod
    def get_by_id(id):
        return Dulce.query.get(id)

    # Actualiza un dulce en la base de datos
    def update(self, marca=None, fecha_elaboracion=None, peso_gramos=None, con_azucar=None, sabor=None, origen=None):
        if marca is not None:
            self.marca = marca
        if fecha_elaboracion is not None:
            # Convert fecha_elaboracion to datetime if it's a string
            if isinstance(fecha_elaboracion, str):
                fecha_elaboracion_datetime = datetime.strptime(fecha_elaboracion, "%Y-%m-%d")
                fecha_elaboracion = fecha_elaboracion_datetime
            self.fecha_elaboracion = fecha_elaboracion
        if peso_gramos is not None:
            self.peso_gramos = peso_gramos
        if con_azucar is not None:
            self.con_azucar = con_azucar
        if sabor is not None:
            self.sabor = sabor
        if origen is not None:
            self.origen = origen
        db.session.commit()
    # Elimina un dulce de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()
