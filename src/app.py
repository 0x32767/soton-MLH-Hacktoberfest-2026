from flask import (
	Flask, redirect, url_for, render_template, request, session
)
import base64
from image_merger import Character

# HEAD, ARM, LEG, TORSO
ALL_PARTS = ["HEAD", "ARM", "LEG", "TORSO"]
parts = {}
images = []


app = Flask(__name__)

@app.route("/")
def index():
    global taken_parts

    part_id = None

    for part in ALL_PARTS:
        if part not in parts:
            part_id = part
            break
    else:
        return "wait"

    return render_template("index.html", part_id=part_id)

@app.route("/submit-part", methods=["POST"])
def submit_part():
    global parts, imgaes

    part_id = request.form["part_id"]
    if part_id in parts:
        return "Part has already been done! Draw faster!  <a href='/'>go back!</a>"

    part = request.form["part"]
    parts[part_id] = part.removeprefix("data:image/png;base64,")

    if len(parts) == len(ALL_PARTS):
        character = Character(
            head_str=parts["HEAD"],
            torso_str=parts["TORSO"],
            arm_str=parts["ARM"],
            leg_str=parts["LEG"],
        )
        data = character.save()
        parts = {}
        images.append(data)

    return render_template("display.html", part_id=part_id, part=part)

@app.route("/done")
def is_done():
    return {"done": len(images)}

@app.route("/see-all")
def see_all():
    res = ""
    for data in images:
        res += f"<img src='data:image/png;base64,{data}'>"
    return res

if __name__ == "__main__":
    app.run(debug=True)
