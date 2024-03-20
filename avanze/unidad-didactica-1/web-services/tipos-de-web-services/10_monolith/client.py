import requests
url = "http://localhost:8000"

# - listar todos los post
response = requests.get(f"{url}/posts")
print(response.text)

print("")
# - obteber el post 2
response = requests.get(f"{url}/post/2")
print(response.text)

# - crear un nuevo post con el titulo...
query = """
    	[
            "title": "mi experiencia",
            "content": "¡Hola mundo! Esta es mi primera publicación en el blog.",
        ],
    
    
"""
titulo= "mi experiencia como dev"
contenido = "es triste, por que no entiendo nada :()"
response = requests.post(f"{url}/posts/", json={'query': query})
# response = requests.post(f"{url}/posts/")

# - actualizar el post 2


# - eliminar el post 2
response = requests.delete(f"{url}/post/2")
print(response.text)



# - listar todos los post
response = requests.get(f"{url}/posts")
print(response.text)
