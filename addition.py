from flask import jsonify

def add(number1, number2):
    try:
        result = float(number1) + float(number2)
        status = 200
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
