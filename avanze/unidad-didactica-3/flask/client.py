import requests
url = "http://localhost:5000/"

get_response = requests.request(method="GET", url=url)
print(get_response.text)


# Definir la consulta GraphQL
query =  {"nombre": "Jose"}

# Solicitud POST al servidor GraphQL
response = requests.get(url+"saludar", params=query)
print(response.text)
