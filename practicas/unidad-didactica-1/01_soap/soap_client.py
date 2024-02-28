from zeep import Client

# cliente apuntando al endpoint del servidor SOAP
client = Client('http://localhost:8000/')

# Llamada al método del servicio SumarNumeros
resultado_suma = client.service.SumarNumeros(n1=31, n2=69)
print("Resultado de la suma:", resultado_suma)

# Llamada al método del servicio EsPalindromo
resultado_palindromo = client.service.EsPalindromo(cadena="reconocer")
print("Es palíndromo?: ", resultado_palindromo)
