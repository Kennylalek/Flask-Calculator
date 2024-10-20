from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/multiply/<int:number1>/<int:number2>')
def multiply(number1, number2):
    result = number1 * number2
    response={
        "status": 200,
        "result": result
    }
    return jsonify(response)