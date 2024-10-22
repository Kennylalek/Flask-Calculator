from flask import Flask, render_template, request
from addition import add
from substraction import subtract
from multiplication import multiply
from division import divide

app = Flask(__name__)

# Default route to render index.html
@app.route('/')
def index():
    return render_template('index.html')

# Route for addition
@app.route('/add/<num1>/<num2>', methods=['GET'])
def perform_add(num1, num2):
    return add(num1, num2)

# Route for subtraction
@app.route('/substract/<num1>/<num2>', methods=['GET'])
def perform_subtract(num1, num2):
    return subtract(num1, num2)


# Route for multiplication
@app.route('/multiply/<num1>/<num2>', methods=['GET'])
def perform_multiply(num1, num2):
    return multiply(num1, num2)

# Route for division
@app.route('/divide/<num1>/<num2>', methods=['GET'])
def perform_divide(num1, num2):
    return divide(num1, num2)

if __name__ == '__main__':
    app.run(debug=True)
