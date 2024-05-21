from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# Base de datos simulada de productos
productos = {}


class Chocolate:
    # constructor para producto
    def __init__(self, tipo, peso, sabor,relleno):
        self.tipo = tipo
        self.peso = peso
        self.sabor = sabor
        self.relleno = relleno

# costructor para producto tableta
class Tableta(Chocolate):
    def __init__(self, peso, sabor):
        super().__init__("tableta", peso, sabor, False)

# constructor para bombon
class Bombon(Chocolate):
    def __init__(self, peso, sabor):
        super().__init__("bombon", peso, sabor, True)

class Trufa(Chocolate):
    def __init__(self, peso, sabor):
        super().__init__("trufa", peso, sabor, True)

# cracion de objetos de tipo de vehiculo
class ProductoFactory:
    @staticmethod
    def create_producto(tipo, peso, sabor):
        if tipo == "tableta":
            return Tableta(peso, sabor)
        elif tipo == "bombon":
            return Bombon(peso, sabor)
        elif tipo == "trufa":
            return Trufa(peso, sabor)
        else:
            raise ValueError("Tipo de chocolate no válido")


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

# las clase para el servicio Chocolate
class ChocolateService:
    # inicializacion de el objeto
    def __init__(self):
        self.factory = ProductoFactory()

    # metodo para agregar un vehiculo a un diccionario.
    def add_producto(self, data):
        # en data se obtiene el cuerpo de la solicitud con none se define si no hay la key
        type = data.get("tipo", None)
        sabor = data.get("sabor", None)
        peso = data.get("peso", None)

        product = self.factory.create_producto(
            type, sabor, peso
        )
        keys = list(productos.keys())
        
        productos[len(productos) + 1] = product
        return product

    def list_products(self):
        # diccionaro de comprension
        return {index: product.__dict__ for index, product in productos.items()}

    # metodo para actualizar la informacon de un producto
    def update_product(self, product_id, data):
        if product_id in productos: #busca el producto por el id
            product = productos[product_id]
            sabor = data.get("sabor", None)
            peso = data.get("peso", None)
            if sabor:
                product.sabor = sabor
            if peso:
                product.peso = peso
            return product
        else:
            raise None

    # metodo para eliminar un producto por id
    def delete_product(self, product_id):
        if product_id in productos:
            del productos[product_id]
            return {"message": "Vehículo eliminado"}
        else:
            return None

# clase para el servidor
class ChocolateRequestHandler(BaseHTTPRequestHandler):
    # metodo para inicializar el servidor
    def __init__(self, *args, **kwargs): # args = parametros y kwargs = diccionaros de parametros
        self.product_service = ChocolateService()
        super().__init__(*args, **kwargs)

    # metodo del servidor para crear un recurso
    def do_POST(self):
        if self.path == "/chocolates":
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.product_service.add_producto(data)
            HTTPDataHandler.handle_response(self, 201, response_data.__dict__)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    # metodo del servidor para obtener datos 
    def do_GET(self):
        if self.path == "/chocolates":
            response_data = self.product_service.list_products()
            HTTPDataHandler.handle_response(self, 200, response_data)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    # metodo del servidor para actualizar un vehiculo por id
    def do_PUT(self):
        if self.path.startswith("/chocolates/"):
            product_id = int(self.path.split("/")[-1])
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.product_service.update_product(product_id, data)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data.__dict__)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "chocolate no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    # metodo del servidor para eliminar un vehiculo por id
    def do_DELETE(self):
        if self.path.startswith("/chocolates/"):
            product_id = int(self.path.split("/")[-1])
            response_data = self.product_service.delete_product(product_id)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "chocolate no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

# funcion para iniciar el servidor
def main():
    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, ChocolateRequestHandler)
        print("Iniciando servidor HTTP en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()

# condicional que verifica si el scrip es main, se le indica que es main y corre las funciones que tiene dentro.
if __name__ == "__main__":
    main()
