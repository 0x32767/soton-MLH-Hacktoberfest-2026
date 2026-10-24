from flask import (
	Flask, redirect, url_for, render_template, request, session
)
import base64
from image_merger import Character

# HEAD, ARM, LEG, TORSO
ALL_PARTS = ["HEAD", "ARM", "LEG", "TORSO"]
parts = {}


app = Flask(__name__)

@app.route("/")
def hello_world():
    global taken_parts

    part_id = None

    for part in ALL_PARTS:
        if part not in parts:
            part_id = part
            break
    else:
        return "wait"

    return render_template("index.html", part_id=part_id)

@app.route("/draw-part")
def index():
    # returns main page for drawing shit
    return "NOT IMPLEMENTED (DRAW)"


@app.route("/submit-part", methods=["POST"])
def submit_part():
    part_id = request.form["part_id"]
    part = request.form["part"]
    parts[part_id] = part.removeprefix("data:image/png;base64,")
    print(part)
    return f"YOUR IMAGE LOOKS LIKE<br><img src='{part}'><br>{part_id=}"


@app.route("/done")
def is_done():
    return {
        "status": len(parts) / len(ALL_PARTS),
        "done": len(parts) == len(ALL_PARTS)
    }

@app.route("/see-result")
def see_result():
    global parts
    character = Character(
        head_str=parts["HEAD"],
        torso_str=parts["TORSO"],
        arm_str=parts["ARM"],
        leg_str=parts["LEG"],
    )
    data = character.save()
    parts = {}
    return f"<img src='data:image/png;base64,{data}'>"


if __name__ == "__main__":
    app.run(debug=True)
