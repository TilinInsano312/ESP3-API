from flask import Flask, request, jsonify
from math import sqrt

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "mensaje": "API REST de Calculadora con Flask",
        "endpoints": {
            "suma": "/api/calculadora/suma",
            "resta": "/api/calculadora/resta",
            "multiplicacion": "/api/calculadora/multiplicacion",
            "division": "/api/calculadora/division",
            "potencia": "/api/calculadora/potencia",
            "raiz": "/api/calculadora/raiz"
        }
    })


def obtener_numeros():
    """
    Valida y obtiene los números enviados en el body JSON.
    Espera:
    {
        "num1": 10,
        "num2": 5
    }
    """
    data = request.get_json()

    if not data:
        return None, jsonify({
            "error": "Debes enviar un body en formato JSON"
        }), 400

    if "num1" not in data or "num2" not in data:
        return None, jsonify({
            "error": "Debes enviar los campos 'num1' y 'num2'"
        }), 400

    try:
        num1 = float(data["num1"])
        num2 = float(data["num2"])
        return (num1, num2), None, None
    except ValueError:
        return None, jsonify({
            "error": "Los valores deben ser numéricos"
        }), 400


@app.route("/api/calculadora/suma", methods=["POST"])
def suma():
    numeros, error, status = obtener_numeros()

    if error:
        return error, status

    num1, num2 = numeros
    resultado = num1 + num2

    return jsonify({
        "operacion": "suma",
        "num1": num1,
        "num2": num2,
        "resultado": resultado
    })


@app.route("/api/calculadora/resta", methods=["POST"])
def resta():
    numeros, error, status = obtener_numeros()

    if error:
        return error, status

    num1, num2 = numeros
    resultado = num1 - num2

    return jsonify({
        "operacion": "resta",
        "num1": num1,
        "num2": num2,
        "resultado": resultado
    })


@app.route("/api/calculadora/multiplicacion", methods=["POST"])
def multiplicacion():
    numeros, error, status = obtener_numeros()

    if error:
        return error, status

    num1, num2 = numeros
    resultado = num1 * num2

    return jsonify({
        "operacion": "multiplicacion",
        "num1": num1,
        "num2": num2,
        "resultado": resultado
    })


@app.route("/api/calculadora/division", methods=["POST"])
def division():
    numeros, error, status = obtener_numeros()

    if error:
        return error, status

    num1, num2 = numeros

    if num2 == 0:
        return jsonify({
            "error": "No se puede dividir entre cero"
        }), 400

    resultado = num1 / num2

    return jsonify({
        "operacion": "division",
        "num1": num1,
        "num2": num2,
        "resultado": resultado
    })


@app.route("/api/calculadora/potencia", methods=["POST"])
def potencia():
    numeros, error, status = obtener_numeros()

    if error:
        return error, status

    num1, num2 = numeros
    resultado = num1 ** num2

    return jsonify({
        "operacion": "potencia",
        "base": num1,
        "exponente": num2,
        "resultado": resultado
    })


@app.route("/api/calculadora/raiz", methods=["POST"])
def raiz():
    """
    Espera:
    {
        "numero": 25
    }
    """
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Debes enviar un body en formato JSON"
        }), 400

    if "numero" not in data:
        return jsonify({
            "error": "Debes enviar el campo 'numero'"
        }), 400

    try:
        numero = float(data["numero"])
    except ValueError:
        return jsonify({
            "error": "El valor debe ser numérico"
        }), 400

    if numero < 0:
        return jsonify({
            "error": "No se puede calcular la raíz cuadrada de un número negativo"
        }), 400

    resultado = sqrt(numero)

    return jsonify({
        "operacion": "raiz cuadrada",
        "numero": numero,
        "resultado": resultado
    })


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Endpoint no encontrado"
    }), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        "error": "Método HTTP no permitido"
    }), 405


if __name__ == "__main__":
    app.run(debug=True)
