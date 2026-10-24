from flask import (
	Flask, redirect, url_for, render_template, request, session
)

# HEAD, ARM, LEG, TORSO
ALL_PARTS = ["HEAD", "ARM", "LEG", "TORSO"]
parts = {}


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/draw-part")
def index():
    # returns main page for drawing shit
    return "NOT IMPLEMENTED (DRAW)"


@app.route("/submit-part", methods=["POST"])
def submit_part():
    print(request.form)
    print(request.files)
    # file = request.files["part"]
    # f.save("images/part.png")
    return "NOT IMPLEMENTED (SEND)"


@app.route("/done")
def is_done():
    return {
        "status": len(parts) / len(ALL_PARTS),
        "done": len(parts) == len(ALL_PARTS)
    }

@app.route("/see-result")
def see_result():
    ...


if __name__ == "__main__":
    app.run(debug=True)
