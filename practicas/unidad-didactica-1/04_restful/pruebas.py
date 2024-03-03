estudiantes = [
    {
        "id": 1,
        "nombre": "Pedrito",
        "apellido": "García",
        "carrera": "Ingeniería de Sistemas",
    },
    {
        "id": 4,
        "nombre": "Aldo",
        "apellido": "García",
        "carrera": "Ingeniería de Sistemas",
    },
    {
        "id": 2,
        "nombre": "Juan",
        "apellido": "Mendoza",
        "carrera": "Ingeniería de Mecanica",
    },
    {
        "id": 3,
        "nombre": "Aldo Vazques",
        "apellido": "Arancivia",
        "carrera": "Ingeniería de Quimica",
    },
    {
        "id": 5,
        "nombre": "María",
        "apellido": "Martínez",
        "carrera": "Economía",
    },
    {
        "id": 6,
        "nombre": "erick",
        "apellido": "poma",
        "carrera": "Economía",
    }
]

# carreras = list({estudiante["carrera"] for estudiante in estudiantes})
# print(carreras)


# estudiante = next(
#                 (estudiante for estudiante in estudiantes if estudiante["id"] == id),
#                 None,
#             )

# print(estudiantes)
# for x in estudiantes:
#     if((x["carrera"])==id):
#         print(x)


id =  "Economía"
estudiante = [estudiante for estudiante in estudiantes if estudiante["carrera"] == "Economía"]
print(estudiante)





a = 1; b =2
def suma(a,b):
    return a+b;

print(suma(a,b) )