# Put your app in here.

from flask import Flask, request
import operations


app = Flask(__name__)


@app.route('/add')
def add():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = operations.add(a, b)
    return str(result)

@app.route('/sub')
def sub():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = operations.sub(a, b)
    return str(result)

@app.route('/mult')
def mult():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = operations.mult(a, b)
    return str(result)

@app.route('/div')
def div():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = operations.div(a, b)
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)