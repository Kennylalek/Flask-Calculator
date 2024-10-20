from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/divide/<int:number1>/<int:number2>')
def divide(number1, number2):
    if number2==0:
        response={
        "status": 400,
        "message": "Division by zero error",
        "result": None
        }
    else:
        result = number1 / number2
        response={
            "status": 200,
            "result": result
        }
    return jsonify(response)
