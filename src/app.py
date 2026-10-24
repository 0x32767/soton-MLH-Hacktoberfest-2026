from flask import (
	Flask, redirect, url_for, render_template, request, session
)
import base64

# HEAD, ARM, LEG, TORSO
games = {} # maps game ID to the done parts
ALL_PARTS = ["HEAD", "ARM", "LEG", "TORSO"]
taken_parts = []
game_id = 0


app = Flask(__name__)

@app.route("/")
def hello_world():
    global taken_parts, game_id

    part_id = None

    for part in ALL_PARTS:
        if part not in taken_parts:
            part_id = part
            break
    else:
        part_id = ALL_PARTS[0]
        taken_parts = [part_id]
        game_id += 1

    return render_template("index.html", game_id=game_id, part_id=part_id)

@app.route("/draw-part")
def index():
    # returns main page for drawing shit
    return "NOT IMPLEMENTED (DRAW)"


@app.route("/submit-part", methods=["POST"])
def submit_part():
    game_id = request.form["game_id"]
    part_id = request.form["part_id"]
    raw_file_data = request.form["part"].removeprefix("data:image/png;base64,")

    with open(f"src/images/{game_id}/{part_id.lower()}.txt", "w") as f:
        f.write(raw_file_data)

    part = request.form["part"]

    print(part)


    if game_id in games:
        game[game_id].append(part)

    return f"YOUR IMAGE LOOKS LIKE<br><img src='{part}'><br>{game_id=}<br>{part_id=}"


@app.route("/done/<game_id>")
def is_done(game_id):
    game_id = int(game_id)
    game = games.get(game_id, 0)
    return {
        "status": len(game) / len(ALL_PARTS),
        "done": len(game) == len(ALL_PARTS)
    }

@app.route("/see-result")
def see_result():
    ...


if __name__ == "__main__":
    app.run(debug=True)
