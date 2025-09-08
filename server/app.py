#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return param

@app.route('/count/<int:n>')
def count(n):
    lines = [str(i) for i in range(n)]
    return "\n".join(lines) + ("\n" if n > 0 else "")

@app.route('/math/<int:num1>/<op>/<int:num2>')
def math(num1, op, num2):
    if op == "+":
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == 'div':
        result = num1 / num2
    elif op == '%':
        result = num1 % num2
    else:
        return "Invalid operation", 404
    
    return str(result)
