from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/dojo')
def success():
    return "Dojo"

# @app.route("/hello/<name>/<id>")
# def hello(name, id):
#     print(name, id)
#     return "Hello, " + name + id


# @app.route("/dojo/<name>/")
# def hello(name, id):
#     print(name, id)
#     return "Dojo" + name + id

# if __name__=="__main__":
#     app.run(debug=True)