from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/operation/add/<int:number1>/<int:number2>')
def add(number1, number2):
    try:
        result = number1 + number2
        status = "success"
    except Exception as e:
        result = 0
        status = f"error: {str(e)}"
    
    response = {
        "status": status,
        "result": result
    }
    return jsonify(response)
# testing
# if __name__ == '__main__':
#     app.run(debug=True)
