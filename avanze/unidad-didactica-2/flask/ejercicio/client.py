import requests
url = "http://localhost:5000/"

n1=5
n2=3
# url_get_res = f"{url}/sumar?num1={n1}&num2={n2}"
url_get_res = f"{url}/sumar?num1={n1}&num2={n2}"
response = requests.request(method="GET", url=url_get_res)
print(response.text)

cad = "reconocer"
url_get_res = f"{url}/palindromo?cadena={cad}"
response = requests.request(method="GET", url=url_get_res)
print(response.text)

cadena = "exepciones"
vocal = "e"
url_get_res = f"{url}/contar?cadena={cadena}&vocal={vocal}"
response = requests.request(method="GET", url=url_get_res)
print(response.text)