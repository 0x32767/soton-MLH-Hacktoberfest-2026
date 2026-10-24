from flask import (
	Flask, redirect, url_for, render_template, request, session
)
import base64
from image_merger import Character

# HEAD, ARM, LEG, TORSO
ALL_PARTS = ["HEAD", "TORSO", "ARM", "LEG"]
body = Character()
images = []


app = Flask(__name__)

@app.route("/")
def index():
    global body

    if body.head is None:
        return render_template("index.html", part_id="HEAD", )
    elif body.torso is None:
        # get preview for head
        
        return render_template("index.html", part_id="TORSO", data=body.get_preview_for_torso())
    elif body.arm is None:
        # get preview for arm
        return render_template("index.html", part_id="ARM", data=body.get_preview_for_arm())
        
    elif body.leg is None:
        
        return render_template("index.html", part_id="LEG", data=body.get_preview_for_leg())
    else:
        return "WAIT"
        # return render_template("index.html", part_id=part_id)

@app.route("/submit-part", methods=["POST"])
def submit_part():
    global body, imgaes

    part_id = request.form["part_id"]
    if getattr(body, part_id.lower()) is not None:
        return render_template("already-done.html")

    part = request.form["part"]
    raw_part = part.removeprefix("data:image/png;base64,")

    if part_id == "HEAD":
        body.add_head(raw_part)
    elif part_id == "TORSO":
        body.add_torso(raw_part)
    elif part_id == "ARM":
        body.add_arm(raw_part)
    elif part_id == "LEG":
        body.add_leg(raw_part)
    else:
        raise Exception(part_id)

    if body.head is not None and body.torso is not None and body.arm is not None and body.leg is not None:
        data = body.save()
        images.append(body.save())
        body = Character()

    return render_template("display.html", part_id=part_id, part=part)

@app.route("/done")
def is_done():
    return {"done": len(images)}

@app.route("/see-all")
def see_all():
    res = ""
    for data in images:
        res += f"<img src='data:image/png;base64,{data}'><br>"
    return res

if __name__ == "__main__":
    app.run(debug=True)
