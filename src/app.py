from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/")
def index():
    # returns main page for drawing shit
    return "index page"


@app.route("/submit-part")
def submit_part():
    ...
