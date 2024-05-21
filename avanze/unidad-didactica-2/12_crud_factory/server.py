from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# Base de datos simulada de vehículos
vehicles = {}


class DeliveryVehicle:
    # constructor para vehiculo
    def __init__(self, vehicle_type, plate_number, capacity):
        self.vehicle_type = vehicle_type
        self.plate_number = plate_number
        self.capacity = capacity

# costructo para motosicleta
class Motorcycle(DeliveryVehicle):
    def __init__(self, plate_number, capacity):
        super().__init__("motorcycle", plate_number, capacity)

# constructor para drone
class Drone(DeliveryVehicle):
    def __init__(self, plate_number, capacity):
        super().__init__("drone", plate_number, capacity)

# cracion de objetos de tipo de vehiculo
class DeliveryFactory:
    @staticmethod
    def create_vehicle(vehicle_type, plate_number, capacity):
        if vehicle_type == "drone":
            return Drone(plate_number, capacity)
        elif vehicle_type == "motorcycle":
            return Motorcycle(plate_number, capacity)
        else:
            raise ValueError("Tipo de vehículo de entrega no válido")


class HTTPDataHandler:
    # En los siguiente metodos se aplica el DRY y la S de Solida
    # metodo para las respuestas
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

    # metodo para leer datos
    @staticmethod
    def handle_reader(handler):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        return json.loads(post_data.decode("utf-8"))

# las clase para el servicio delivery
class DeliveryService:
    # inicializacion de el objeto
    def __init__(self):
        self.factory = DeliveryFactory()

    # metodo para agregar un vehiculo a un diccionario.
    def add_vehicle(self, data):
        # en data se obtiene el cuerpo de la solicitud con none se define si no hay la key
        vehicle_type = data.get("vehicle_type", None)
        plate_number = data.get("plate_number", None)
        capacity = data.get("capacity", None)

        delivery_vehicle = self.factory.create_vehicle(
            vehicle_type, plate_number, capacity
        )
        vehicles[len(vehicles) + 1] = delivery_vehicle
        return delivery_vehicle

    def list_vehicles(self):
        # diccionaro de comprension
        return {index: vehicle.__dict__ for index, vehicle in vehicles.items()}

    # metodo para actualizar la informacon de un vehiculo
    def update_vehicle(self, vehicle_id, data):
        if vehicle_id in vehicles: #busca el vehiculo por el id
            vehicle = vehicles[vehicle_id]
            plate_number = data.get("plate_number", None)
            capacity = data.get("capacity", None)
            if plate_number:
                vehicle.plate_number = plate_number
            if capacity:
                vehicle.capacity = capacity
            return vehicle
        else:
            raise None

    # metodo para eliminar un vehiculo por id
    def delete_vehicle(self, vehicle_id):
        if vehicle_id in vehicles:
            del vehicles[vehicle_id]
            return {"message": "Vehículo eliminado"}
        else:
            return None

# clase para el servidorr
class DeliveryRequestHandler(BaseHTTPRequestHandler):
    # metodo para inicializar el servidor
    def __init__(self, *args, **kwargs): # args = parametros y kwargs = diccionaros de parametros
        self.delivery_service = DeliveryService()
        super().__init__(*args, **kwargs)

    # metodo del servidor para crear un recurso
    def do_POST(self):
        if self.path == "/deliveries":
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.delivery_service.add_vehicle(data)
            HTTPDataHandler.handle_response(self, 201, response_data.__dict__)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    # metodo del servidor para obtener datos 
    def do_GET(self):
        if self.path == "/deliveries":
            response_data = self.delivery_service.list_vehicles()
            HTTPDataHandler.handle_response(self, 200, response_data)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    # metodo del servidor para actualizar un vehiculo por id
    def do_PUT(self):
        if self.path.startswith("/deliveries/"):
            vehicle_id = int(self.path.split("/")[-1])
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.delivery_service.update_vehicle(vehicle_id, data)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data.__dict__)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "Vehículo no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    # metodo del servidor para eliminar un vehiculo por id
    def do_DELETE(self):
        if self.path.startswith("/deliveries/"):
            vehicle_id = int(self.path.split("/")[-1])
            response_data = self.delivery_service.delete_vehicle(vehicle_id)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "Vehículo no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

# funcion para iniciar el servidor
def main():
    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, DeliveryRequestHandler)
        print("Iniciando servidor HTTP en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()

# condicional que verifica si el scrip es main, se le indica que es main y corre las funciones que tiene dentro.
if __name__ == "__main__":
    main()
