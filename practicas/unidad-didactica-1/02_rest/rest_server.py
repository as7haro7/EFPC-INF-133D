from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# Lista de estudiantes
estudiantes = [
    {
        "id": 1,
        "nombre": "Pablo",
        "apellido": "Mendoza",
        "carrera": "Ingeniería Mecanica",
    },
    {
        "id": 2,
        "nombre": "Elder",
        "apellido": "Gonzales",
        "carrera": "Ingeniería Mecanica",
    },
    {
        "id": 3,
        "nombre": "Elsa",
        "apellido": "Apaza",
        "carrera": "Ingeniería Quimica",
    },
    {
        "id": 4,
        "nombre": "Alejandra",
        "apellido": "Quispe",
        "carrera": "Ingeniería Quimica",
    },
    {
        "id": 5,
        "nombre": "Pool",
        "apellido": "Solares",
        "carrera": "Ingeniería Electronica",
    },
]

class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/lista_estudiantes':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
        elif self.path == '/buscar_nombre':
            nombres_con_P = [estudiante["nombre"] for estudiante in estudiantes if estudiante["nombre"].startswith("P")]
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(nombres_con_P).encode('utf-8'))
        elif self.path == '/contar_carreras':
            carreras = {}
            for estudiante in estudiantes:
                carrera = estudiante["carrera"]
                carreras[carrera] = carreras.get(carrera, 0) + 1
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(carreras).encode('utf-8'))
        elif self.path == '/total_estudiantes':
            total = len(estudiantes)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"total_estudiantes": total}).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode('utf-8'))
            
    def do_POST(self):
        if self.path == '/agrega_estudiante':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode('utf-8'))
            post_data['id'] = len(estudiantes) + 1
            estudiantes.append(post_data)
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode('utf-8'))
            
def run_server(port=8000):
    try:
        server_address = ('', port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f'Iniciando servidor web en http://localhost:{port}/')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Apagando servidor web')
        httpd.socket.close()

if __name__ == "__main__":
    run_server()
