from flask import (
	Flask, redirect, url_for, render_template, request, session
)

parts = {}


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/draw-part")
def index():
    # returns main page for drawing shit
    return "NOT IMPLEMENTED (DRAW)"


@app.route("/submit-part")
def submit_part():
    return "NOT IMPLEMENTED (SEND)"
