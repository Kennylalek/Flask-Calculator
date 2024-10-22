from flask import jsonify

def multiply(number1, number2):
    result = number1 * number2
    response={
        "status": 200,
        "result": result
    }
    return jsonify(response)
