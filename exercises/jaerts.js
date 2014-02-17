var objects = new Array;
for (i = 0; i < 1000; i++) {
    var circle = new Path.Circle(new Point(Math.random()*500, Math.random()*500), Math.random()*20)
    circle.fillColor = 'lightgrey';
    circle.strokeColor = 'black';
    circle.opacity = 0.5;
    objects.push(circle);
}

var mouseDownPosition;
var mouseDragPosition;
var selectionRectangle;
function onMouseDown(event) {
    mouseDownPosition = event.point;
}
function onMouseDrag(event) {
    mouseDragPosition = event.point;
    if (selectionRectangle) { selectionRectangle.remove(); }
    selectionRectangle = new Path.Rectangle(mouseDownPosition, mouseDragPosition);
    selectionRectangle.strokeColor = 'grey';
    
    // This is slow because has to go over all objects with every pixel dragged
    for (var i = 0; i < objects.length; i++ ) {
        if ( selectionRectangle.bounds.intersects(objects[i].bounds) ) {
            objects[i].fillColor = 'red';
        } else {
            objects[i].fillColor = 'lightgrey';
        }
    }
}
function onMouseUp(event) {
    selectionRectangle.remove();
}
