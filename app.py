from flask import Flask, render_template, jsonify

app = Flask(__name__)

"""
example for operations endpoint :
@app.route(/operation/<number1>/<number2>)
def operation(number1, number2) :
    try :
        do the operation here

        result = 
        status =

    except Exception :
        handle exception
        
        result = 0 
        status =

    result = {
        "status" : status,
        "result" : result
    }

    return jsonify(result)
        
"""