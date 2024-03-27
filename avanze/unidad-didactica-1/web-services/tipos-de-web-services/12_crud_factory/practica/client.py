import requests
import json

url = "http://localhost:8000/chocolates"
headers = {"Content-Type": "application/json"}

print("\n"," -- POST --","\n")
# POST /chocolates
chocolate_data = {
    "tipo": "tableta",
    "peso": 10,
    "sabor": "pila"
}
response = requests.post(url=url, json=chocolate_data, headers=headers)
print(response.json())

chocolate_data = {
    "tipo": "bombon",
    "peso": 1,
    "sabor": "nose"
}
response = requests.post(url=url, json=chocolate_data, headers=headers)
print(response.json())

chocolate_data = {
    "tipo": "trufa",
    "peso": 102,
    "sabor": "algo"
}
response = requests.post(url=url, json=chocolate_data, headers=headers)
print(response.json())

print("\n"," -- GET --","\n")
# GET /chocolates
response = requests.get(url=url)
print(response.json())

print("\n"," -- PUT --","\n")
# PUT /chocolates/{product_id}
product_id_to_update = 1
updated_product_data = {
    "sabor": "XYZ789"
}
response = requests.put(f"{url}/{product_id_to_update}", json=updated_product_data)
print("Chocolate actualizado:", response.json())

print("\n"," -- GET --","\n")
# GET /chocolates
response = requests.get(url=url)
print(response.json())

print("\n"," -- DELETE --","\n")
# DELETE /chocolates/{product_id}
product_id_to_delete = 3
response = requests.delete(f"{url}/{product_id_to_delete}")
print("chocolate eliminado:", response.json())

print("\n"," -- DELETE --","\n")
# GET /chocolates
response = requests.get(url=url)
print(response.json())