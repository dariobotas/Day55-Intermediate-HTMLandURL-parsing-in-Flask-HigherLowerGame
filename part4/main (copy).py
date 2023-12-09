from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
  return '<h1 style="color:blue; text-align: center">Hello World!</h1>'\
  '<p>This is a paragraph.</p>'\
  '<img src="https://www.w3schools.com/images/w3schools_green.jpg" alt="W3Schools.com" width=288>'
  #return "<h1>Hello, World!</h1>"


@app.route('/bye')
def bye():
    return "<u><em><b>Bye!</b></em></u>"


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
