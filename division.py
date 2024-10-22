from flask import jsonify

def divide(number1, number2):
    try:
        result = number1 / number2
        response = {
            "status": 200,
            "result": result
        }
    except ZeroDivisionError:
        response = {
            "status": 400,
            "message": "division by zero error",
            "result": None
        }
    return jsonify(response)
