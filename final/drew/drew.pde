void setup() {
size(400, 600);
background(255);
smooth();
}

void draw() {
stroke(0);

line(pmouseX, pmouseY, mouseX, mouseY);
}
