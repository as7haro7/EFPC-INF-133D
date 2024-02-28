import requests

url = "http://localhost:8000/"

# GET consulta a la ruta /lista_estudiantes
ruta_get_lista_estudiantes = url + "lista_estudiantes"
get_response_lista_estudiantes = requests.get(ruta_get_lista_estudiantes)
print("Lista de estudiantes:")
print(get_response_lista_estudiantes.json())

# GET consulta a la ruta /buscar_nombre
ruta_get_buscar_nombre = url + "buscar_nombre"
get_response_buscar_nombre = requests.get(ruta_get_buscar_nombre)
print("Nombres que empiezan con la letra 'P':")
print(get_response_buscar_nombre.json())

# GET consulta a la ruta /contar_carreras
ruta_get_contar_carreras = url + "contar_carreras"
get_response_contar_carreras = requests.get(ruta_get_contar_carreras)
print("Cantidad de estudiantes por carrera:")
print(get_response_contar_carreras.json())

# GET consulta a la ruta /total_estudiantes
ruta_get_total_estudiantes = url + "total_estudiantes"
get_response_total_estudiantes = requests.get(ruta_get_total_estudiantes)
print("Total de estudiantes:")
print(get_response_total_estudiantes.json())

# POST agrega un nuevo estudiante por la ruta /agrega_estudiante
ruta_post_agrega_estudiante = url + "agrega_estudiante"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}

post_response_agrega_estudiante = requests.post(ruta_post_agrega_estudiante, json=nuevo_estudiante)
print("Respuesta de agregar estudiante:")
print(post_response_agrega_estudiante.json())
