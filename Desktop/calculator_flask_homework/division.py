from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/divide/<int:number1>/<int:number2>')
def divide(number1, number2):
    if number2 == 0:
        response ={
            "status": 400,
            "message": "Division by zero!",
            "result": None,
        }
        return jsonify(response),
    else:
        result = number1 / number2
        response = {
            "status": 200,
            "result": result
        }
        return jsonify(response)
    

    