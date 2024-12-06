from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/<opt>/<int:a>/<int:b>')
def calculate(opt, a, b):
    result = None
    if opt == 'add':
        result = a + b
    elif opt == 'sub':
        result = a - b
    elif opt == 'mul':
        result = a * b
    elif opt == 'div':
        if b != 0:
            result = a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"
    
    return str(result)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
