from flask import Flask, request, render_template

app = Flask(__name__)

# Define the calculator function with improved error handling
def calculate(a, b, operation):
    try:
        a = float(a)
        b = float(b)
        if operation == 'add':
            result = a + b
        elif operation == 'subtract':
            result = a - b
        elif operation == 'multiply':
            result = a * b
        elif operation == 'divide':
            if b == 0:
                result = "Division by zero is not allowed"
            else:
                result = a / b
        else:
            result = "Invalid operation"
        return result
    except ValueError:
        return "Invalid input"

# Define the route for the calculator form
@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        a = request.form['a']
        b = request.form['b']
        operation = request.form['operation']
        result = calculate(a, b, operation)
    return render_template('calculator.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
