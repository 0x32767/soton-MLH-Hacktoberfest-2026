part_id = document.getElementById('part_id').innerHTML;
console.log("Editing: ", part_id);

paper.install(window);
// Keep global references to both tools, so the HTML
// links below can access them.
var tool1, tool2;

window.onload = function() {
	paper.setup('myCanvas');

	// Create two drawing tools.
	// tool1 will draw straight lines,
	// tool2 will draw clouds.

	// Both share the mouseDown event:
	var path;
	function onMouseDown(event) {
		colour = document.getElementById('colour-select').value;
		width = document.getElementById('width-select').value;
		console.log(colour,width);
		path = new Path();
		path.strokeColor = colour;
		path.strokeWidth = width;
		
		path.add(event.point);
	}

	tool1 = new Tool();
	tool1.onMouseDown = onMouseDown;

	tool1.onMouseDrag = function(event) {
		path.add(event.point);
	}

	tool2 = new Tool();
	tool2.minDistance = 20;
	tool2.onMouseDown = onMouseDown;

	tool2.onMouseDrag = function(event) {
		// Use the arcTo command to draw cloudy lines
		path.arcTo(event.point);
	}
}

function submit_canvas() {
	let canvas = document.getElementById('myCanvas');
	let canvasURL = canvas.toDataURL("image/png");
	document.getElementById("image").value = canvasURL;
}
