from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

# función del servicio para sumar dos números
def suma_numeros(num1, num2):
    return num1 + num2

# función del servicio para verificar si una cadena es un palíndromo
def es_palindromo(cadena):
    return cadena == cadena[::-1]

# ruta del servidor SOAP
dispatcher = SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)

# nuevos servicios
dispatcher.register_function(
    "SumarNumeros",
    suma_numeros,
    returns={"resultado": int},
    args={"num1": int, "num2": int},
)

dispatcher.register_function(
    "EsPalindromo",
    es_palindromo,
    returns={"es_palindromo": bool},
    args={"cadena": str},
)

# Inicio servidor HTTP
server = HTTPServer(("0.0.0.0", 8000), SOAPHandler)
server.dispatcher = dispatcher
print("Servidor SOAP iniciado en http://localhost:8000/")
server.serve_forever()
