myCanvas.width = window.innerWidth;
myCanvas.height = window.innerHeight;

A = {x: 210, y: 130};
B = {x: 150, y: 250};
C = {x: 50, y: 100};
D = {x: 250, y: 200};

const ctx = myCanvas.getContext("2d");

ctx.beginPath();

ctx.moveTo(A.x, A.y);
ctx.lineTo(B.x, B.y);

ctx.moveTo(C.x, C.y);
ctx.lineTo(D.x, D.y);

ctx.stroke();

drawDot(A, "A");
drawDot(B, "B");
drawDot(C, "C");
drawDot(D, "D");


r_t = 0.334;
M = {
	x: lerp(A.x, B.x, r_t),
	y: lerp(A.y, B.y, r_t)
};

r_u = 0.698;
N = {
	x: lerp(C.x, D.x, r_u),
	y: lerp(C.y, D.y, r_u)
};

console.log("lerp A.x, B.x: " + lerp(A.x, B.x, r_t));
console.log("lerp A.y, B.y: " + lerp(A.y, B.y, r_t));
console.log("lerp C.x, D.x: " + lerp(C.x, D.x, r_u));
console.log("lerp C.y, D.y: " + lerp(C.y, D.y, r_u));
console.log("##############")
console.log("A.x A.y: " + A.x + ", " + A.y);
console.log("B.x B.y: " + B.x + ", " + B.y);
console.log("C.x C.y: " + C.x + ", " + C.y);
console.log("D.x D.y: " + D.x + ", " + D.y);

drawDot(M, "M");
drawDot(N, "N");

/*

t = ?
u = ?

*/





function drawDot(point, label) {
	ctx.beginPath();
	ctx.fillStyle = "white";
	ctx.arc(point.x, point.y, 10, 0, Math.PI*2);
	ctx.fill();
	ctx.stroke();
	ctx.fillStyle = "black"
	ctx.textAlign = "center"
	ctx.textBaseline = "middle"
	ctx.font = "Bold 14px Arial"
	ctx.fillText(label, point.x, point.y)
};


function lerp(a, b, t) {
	return a + t * (b - a);
};


