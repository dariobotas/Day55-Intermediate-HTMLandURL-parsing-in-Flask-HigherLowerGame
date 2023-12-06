from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello, World!"


@app.route('/bye')
def bye():
    return "Bye!"


@app.route('/username/<name>') # route with variables. The updates to the route need to refresh the server.
def greet(name):
    return f"Hello {name}"


@app.route('/username/<path:name>') # route with variables. The updates to the route need to refresh the server.
def greet(name):
    return f"Hello {name}"


@app.route('/username/<name>/<int:number>') # route with variables. The updates to the route need to refresh the server.
def greet(name, number):
    return f"Hello {name}, you are {number} years old!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True) # activate debug: debug=True -> able to make changes to flask without need to refresh the server
    # http://192.168.204.133:8080/
