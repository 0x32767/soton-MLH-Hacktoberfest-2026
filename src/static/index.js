part_id = document.getElementById('part_id').innerHTML;
console.log("Editing: ", part_id);

let overlap = 50;
let part_canvases = {"HEAD": [650,650], "TORSO": [750,650], "LEG": [750,1100], "ARM": [750,600]};
let canvas = document.getElementById('myCanvas');
canvas.height = part_canvases[part_id][0];
canvas.width = part_canvases[part_id][1];

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
	function mouseDownCircle(event) {
		colour = document.getElementById('colour-select').value;
		width = document.getElementById('width-select').value;
		path = new Path.Circle(event.point,width*3);
		path.strokeColor = colour;
	}
	function mouseDownSquare(event) {
		colour = document.getElementById('colour-select').value;
		width = document.getElementById('width-select').value;
		path = new Path.Rectangle(new Point(event.point.x-width,event.point.y-width),new Size(width*5,width*5));
		path.strokeColor = colour;
	}
	function mouseDownPumpkin(event) {
		width = document.getElementById('width-select').value;
		let raster = new Raster('pumpkin');
		raster.size = new Size(width*15,width*15);
		raster.position = event.point;
	}
	function mouseDownWeb(event) {
		width = document.getElementById('width-select').value;
		let raster = new Raster('web');
		raster.size = new Size(width*15,width*15);
		raster.position = event.point;
	}
	function mouseDownSkull(event) {
		width = document.getElementById('width-select').value;
		let raster = new Raster('skull');
		raster.size = new Size(width*15,width*15);
		raster.position = event.point;
	}

	tool1 = new Tool();
	tool1.onMouseDown = onMouseDown;
	tool1.onMouseDrag = function(event) { path.add(event.point); }

	tool2 = new Tool();
	tool2.minDistance = 20;
	tool2.onMouseDown = onMouseDown;
	tool2.onMouseDrag = function(event) { path.arcTo(event.point); }

	tool3 = new Tool();
	tool3.onMouseDown = mouseDownCircle;
	tool4 = new Tool();
	tool4.onMouseDown = mouseDownSquare;
	tool5 = new Tool();
	tool5.onMouseDown = mouseDownPumpkin;
	tool6 = new Tool();
	tool6.onMouseDown = mouseDownWeb;
	tool7 = new Tool();
	tool7.onMouseDown = mouseDownSkull;
}

function submit_canvas() {
	let canvas = document.getElementById('myCanvas');
	let canvasURL = canvas.toDataURL("image/png");
	document.getElementById("image").value = canvasURL;
}
