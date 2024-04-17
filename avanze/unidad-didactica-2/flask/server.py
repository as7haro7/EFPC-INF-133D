# importando la clase de Flask del paquete flask
# para los query params request,jsonify
from flask import Flask,request,jsonify

# instancia de la clase flask desntro de este script con __name__
app = Flask(__name__)

# decorador, por defecto en get
@app.route('/')
def hello_world():
    return '!hola, mundo!'

@app.route('/saludar',methods=['GET'])
def saludar():
    nombre = request.args.get("nombre")
    if not nombre:
        return (
            jsonify({"error": "Se requiere un nombre en los parámetros de la URL."}),
            400,
        )
    # Retorna un saludo personalizado utilizando el nombre recibido como parámetro.
    return jsonify({"mensaje": f"¡Hola, {nombre}!"})
if __name__ == '__main__':
    app.run()