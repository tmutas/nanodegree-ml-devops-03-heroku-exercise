from flask import Flask

flaskapp = Flask(__name__)

@flaskapp.route("/")
def hello_world():
    return (
        "<h1>Hello world!</h1>"
        "<p>This a test for deploying a web app through Heroku</p>"
    )