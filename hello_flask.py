from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_flask():
    return "<p>Hello, Flask!</p>"

@app.route("/home")
def home():
    return "<h4>Welcome to app home</h4>"

@app.route("/about")
def foo():
    return "<p>This is a testing development</p>"