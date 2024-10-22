from flask import jsonify

def divide(number1, number2):
    try:
        result = float(number1) / float(number2)
        response = {
            "status": 200,
            "result": result
        }
    except Exception as e:
        result = 0
        status = f"error: {str(e)}"
        response = {
        "status": status,
        "result": result
        }
    except ZeroDivisionError:
        response = {
            "status": 400,
            "message": "division by zero error",
            "result": None
        }
    return jsonify(response)
