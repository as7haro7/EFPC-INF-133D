# importando la clase de Flask del paquete flask
# para los query params request,jsonify
from flask import Flask,request,jsonify

# instancia de la clase flask desntro de este script con __name__
app = Flask(__name__)

# decorador, por defecto en get
@app.route('/')
def hello_world():
    return '!hola, mundo!'

def sumar(a,b):
    return (a+b)


@app.route('/sumar',methods=['GET'])
def sumar():
    num1=request.args.get("num1")
    num2=request.args.get("num2")
    suma = int(num1)+int(num2)
    if (not num1) and (not num2):
        return (
            jsonify({"error": "Se requiere un nombre en los parámetros de la URL."}),
            400,
        )   
    return jsonify({"mensaje": f"suma: {suma}"})

@app.route('/palindromo',methods=['GET'])
def palindromo():
    cadena=request.args.get("cadena") 
    
    if (not cadena):
        return (
            jsonify({"error": "Se requiere un nombre en los parámetros de la URL."}),
            400,
        )   
    return jsonify({"mensaje": f"es palindromo: {cadena == cadena[::-1]}"})

def conteo(palabra,vocal):
    s=0
    for c in palabra:
        if c == vocal:
            s+=1
    return s

@app.route('/contar',methods=['GET'])
def contar():
    cadena=request.args.get("cadena") 
    vocal=request.args.get("vocal") 
    
    if (not cadena) and (not vocal):
        return (
            jsonify({"error": "Se requiere un nombre en los parámetros de la URL."}),
            400,
        )   
    return jsonify({"mensaje": f" contar: {conteo(cadena,vocal)}"})

if __name__ == '__main__':
    app.run()