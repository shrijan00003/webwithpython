from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "Hello world!!!!!"

# The following route is for sepecific route 
# @app.route("/david")
# def david():
#     return "Hello David!!!!!"

# The route for generic one
@app.route("/<string:name>")
def hello(name):
    name=name.capitalize()
    return f"<h1>Hello,{name}!!!</h1>"

